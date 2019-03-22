from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from gatetrack.choices import *

# Create your models here.

#
class Cluster(models.Model):
    name = models.CharField(default="Cluster 10", max_length=50)
    fields = models.TextField(default="D28, Temana")
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE) #link the user to the cluster
    designation = models.CharField(default="Manager", max_length=100)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    name = models.CharField(default="D28 Phase 1", max_length=50)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    cluster = models.ForeignKey('Cluster', on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True, null=True)
    project_type = models.CharField(choices=TYPE_OF_PROJECT, default="Field Development Plan", max_length=100)
    project_info = models.TextField(default="key in your project information over here")
    type_of_scope = models.CharField(choices=SCOPE_OF_WORK, default="Dev/Re-eval/Model", max_length=100)

    def __str__(self):
        return self.name