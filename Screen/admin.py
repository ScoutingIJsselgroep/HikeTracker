from django.contrib import admin

# Register your models here.
from .models import Checkpoint, Team, Visit, Route

admin.site.register(Checkpoint)
admin.site.register(Team)
admin.site.register(Visit)
admin.site.register(Route)