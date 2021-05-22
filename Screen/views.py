from .models import Checkpoint, Team, Visit, Route

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing 
from reportlab.graphics.barcode.qr import QrCodeWidget 
from reportlab.graphics import renderPDF
from reportlab.lib.units import cm


import datetime

import hashlib 


def index(request):
    try: 
        team = Team.objects.get(uuid=request.COOKIES['registration'])
        team_visited = Visit.objects.filter(team=team).order_by('team__name')
        return render(request, "base.html", {'team': team, 'team_visited': team_visited})
    except:
        return render(request, "base.html")
    
def session(request, slug):
    try: 
        team = Team.objects.get(uuid=slug)
    except:
        return render(request, "not_registered.html")

    team_visited = Visit.objects.filter(team=team).order_by('team__name')

    response = render(request, "registered.html", {'team': team, 'team_visited': team_visited})
    
    response.set_cookie('registration', slug)

    return response 

def route(request):
    if 'registration' not in request.COOKIES:
        return render(request, "not_registered.html")
    team = Team.objects.get(uuid=request.COOKIES['registration'])

    # Get route identifier
    route_id = Team.objects.get(uuid=request.COOKIES['registration']).route

    # Get route
    route = Route.objects.get(uuid=route_id.uuid)

    # Render page
    return render(request, "route.html", {"route": route, "team": team, 'isadmin': request.user.is_authenticated})


def checkpoint(request, slug):
    if 'registration' not in request.COOKIES:
        return render(request, "not_registered.html")

    team = Team.objects.get(uuid=request.COOKIES['registration'])

    checkpoint = Checkpoint.objects.filter(uuid=slug)

    if checkpoint.exists():
        checkpoint = checkpoint.get()
        try: 
            Visit.objects.create(checkpoint=checkpoint, team=team, date_visited=datetime.datetime.now())
        except:
            pass
        team_visited = Visit.objects.filter(team=team).order_by('team__name')

        number_of_teams = Team.objects.count()
        teams_visited = Visit.objects.filter(checkpoint__name=checkpoint.name)
        number_of_teams_visited = teams_visited.count()

        return render(request, "checkpoint.html", {'team_visited': team_visited, 'current_url': request.get_full_path(), 'teams_visited': teams_visited, 'checkpoint': checkpoint, 'team': team, 'number_of_teams': number_of_teams, 'number_of_teams_visited':number_of_teams_visited})
    else:
        team_visited = Visit.objects.filter(team=team).order_by('team__name')

        return render(request, "checkpoint_notfound.html", {'team_visited': team_visited, 'team': team})

def checkpoints(request):
    if 'registration' not in request.COOKIES:
        return render(request, "not_registered.html")

    team = Team.objects.get(uuid=request.COOKIES['registration'])
    team_visited = Visit.objects.filter(team=team).order_by('checkpoint__name')
    return render(request, "checkpoints.html", {'team_visited': team_visited, 'team': team})
    
def progress(request):
    if 'registration' not in request.COOKIES:
        return render(request, "not_registered.html")

    # Get route identifier
    route_id = Team.objects.get(uuid=request.COOKIES['registration']).route

    # Generate matrix
    current_team = Team.objects.get(uuid=request.COOKIES['registration']) 
    teams = Team.objects.filter(route=route_id).all()
    checkpoints = Checkpoint.objects.filter(route=route_id).order_by('name')
    progress = [{"name": team.name, "uuid": team.uuid, "checkpoints": [{"name": checkpoint.name, "uuid": checkpoint.uuid, "visited": False} for checkpoint in checkpoints]} for team in teams]

    # Apply visits
    visits = Visit.objects.all().select_related('team', 'checkpoint')
    for visit in visits:
        for team in progress:
            if team["uuid"] == visit.team.uuid:
                for checkpoint in team["checkpoints"]:
                    if checkpoint["uuid"] == visit.checkpoint.uuid:
                        checkpoint["visited"] = True
                        checkpoint["date_visited"] = visit.date_visited

    return render(request, "progress.html", {'progress': progress, 'team': current_team})

def generate_qr(request, route_id):
    if not request.user.is_authenticated:
        return render(request, "not_registered.html")
        
    route = Route.objects.get(uuid=route_id)
    # Get routes
    checkpoints = Checkpoint.objects.filter(route=route_id).order_by('name')

    # Get teams
    teams = Team.objects.filter(route=route_id).all()

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{route.name}.pdf"'

    p = canvas.Canvas(response)

    for checkpoint in checkpoints:
        qrw = QrCodeWidget(f"https://piraat-hike-tracker.herokuapp.com/register/{checkpoint.uuid}") 
        b = qrw.getBounds()
        qrw.barHeight = 20*cm
        qrw.barWidth = 20*cm

        d = Drawing(20*cm, 20*cm) 
        d.add(qrw)
        p.setFont('Helvetica',20)
        p.drawCentredString(21*cm/2, 24*cm, "CHECKPOINT")
        p.setFont('Helvetica',30)
        p.drawCentredString(21*cm/2, 22*cm, checkpoint.name)
        p.setFont('Helvetica',15)
        p.drawCentredString(21*cm/2, 20*cm, f"QR code voor {route.name}. S.v.p. laten hangen.")

        renderPDF.draw(d, p, 0, 0)
        
        p.showPage()
    
    for team in teams:
        qrw = QrCodeWidget(f"https://piraat-hike-tracker.herokuapp.com/register/{team.uuid}") 
        b = qrw.getBounds()

        qrw.barHeight = 10*cm
        qrw.barWidth = 10*cm

        d = Drawing(10*cm, 10*cm) 
        d.add(qrw)
        p.setFont('Helvetica',20)
        p.drawCentredString(21*cm/2, 24*cm, "TEAM")
        p.setFont('Helvetica',30)
        p.drawCentredString(21*cm/2, 22*cm, team.name)
        p.setFont('Helvetica',15)
        p.drawCentredString(21*cm/2, 20*cm, f"Scan mij om je telefoon te registreren!")

        renderPDF.draw(d, p, 5*cm, 0)
        
        p.showPage()
    
    p.save()
    return response