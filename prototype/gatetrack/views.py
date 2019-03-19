from django.shortcuts import render
from .models import Cluster, UserProfile, Project
from django.http import Http404

# Create your views here.

def index(request):
    try:
        clusters = Cluster.objects.all()
    except Cluster.DoesNotExist:
        raise Http404("Error 404")
    return render(request, 'gatetrack/index.html', { 'clusters' : clusters })