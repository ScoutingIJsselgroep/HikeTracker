from .models import Checkpoint, Team, Visit

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

import datetime

import hashlib 


def index(request):
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

        return render(request, "checkpoint.html", {'team_visited': team_visited, 'teams_visited': teams_visited, 'checkpoint': checkpoint, 'team': team, 'number_of_teams': number_of_teams, 'number_of_teams_visited':number_of_teams_visited})
    else:
        team_visited = Visit.objects.filter(team=team).order_by('team__name')

        return render(request, "checkpoint_notfound.html", {'team_visited': team_visited, 'team': team})