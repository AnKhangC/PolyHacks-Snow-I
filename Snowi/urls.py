from django.contrib import admin
from django.urls import path
from Maps import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('map/', views.google_map, name='google_map'),
]
