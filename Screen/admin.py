from django.contrib import admin

# Register your models here.
from .models import Checkpoint, Team, Visit

admin.site.register(Checkpoint)
admin.site.register(Team)
admin.site.register(Visit)