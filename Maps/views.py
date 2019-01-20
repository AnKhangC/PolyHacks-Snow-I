from django.shortcuts import render
from django.http import HttpResponse
from .models import Tractor, Coord, Route, parking
from django.template import loader
from django.http import Http404


def google_map(request):
    route1 = Route.objects.get(pk=1)
    route2 = Route.objects.get(pk=2)
    parking1 = parking.objects.get(pk=89)
    parkings = parking.objects.all()
    template = loader.get_template('gMap.html')
    context = {
        'route1': route1,
        'route2': route2,
        'parkings': parkings,
        'parking1': parking1
    }
    return HttpResponse(template.render(context, request))

