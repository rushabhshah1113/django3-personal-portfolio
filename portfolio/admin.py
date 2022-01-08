from django.contrib import admin
# Need to specify which models we want to show up inside admin
from .models import Project

# Tell admin you want to see Project model inside admin
admin.site.register(Project)
