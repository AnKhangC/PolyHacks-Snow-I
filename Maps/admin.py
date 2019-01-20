from django.contrib import admin
from .models import Tractor, Coord, Route, parking


admin.site.register(Tractor)
admin.site.register(Coord)
admin.site.register(Route)
admin.site.register(parking)