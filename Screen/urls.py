from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('checkpoint/<slug:slug>', views.checkpoint, name='secret'),
    path('register/<slug:slug>', views.session, name='session')
]