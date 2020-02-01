from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from pages.models import Camera
# Create your views here.
@login_required(login_url = 'login')
def alerts(request):
    cameras = Camera.objects.all()
    context = {
        'cameras':cameras,
    }
    return render(request, 'deploy/alerts.html',context)



@login_required(login_url = 'login')
def maps(request, pk):
    camera = Camera.objects.get(id=pk)
    # long = 77.212335
    # lat = 28.641221
    long = camera.longitude
    lat =  camera.latitude
    location = camera.location

    context = {
        'lat':lat,
        'long':long,
        'location':location,
        
    }

    return render(request, 'deploy/map.html',context)