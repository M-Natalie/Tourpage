from django.shortcuts import render
from .models import Place

# Create your views here.

def places(request):
    place_objects = Place.objects.all()
    return render(request, 'places.html', {'places': place_objects})

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)