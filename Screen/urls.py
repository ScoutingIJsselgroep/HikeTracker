from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('checkpoint/<slug:slug>', views.checkpoint, name='secret'),
    path('checkpoints', views.checkpoints, name='checkpoints'),
    path('register/<slug:slug>', views.session, name='session'),
    path('route', views.route, name='route'),
    path('progress', views.progress, name='progress'),
    path('generateqr/<slug:route_id>', views.generate_qr, name='generate_qr'),
]