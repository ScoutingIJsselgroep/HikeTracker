from django.contrib import admin

# Register your models here.
from .models import Checkpoint, Team

admin.site.register(Checkpoint)
admin.site.register(Team)