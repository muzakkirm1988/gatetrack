from django.contrib import admin
from .models import Cluster, UserProfile, Project

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Cluster)
admin.site.register(Project)