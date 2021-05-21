from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('checkpoint/<slug:slug>', views.checkpoint, name='secret'),
    path('checkpoints', views.checkpoints, name='checkpoints'),
    path('register/<slug:slug>', views.session, name='session'),
    path('progress', views.progress, name='progress')
]