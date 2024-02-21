from django.urls import path
from .views import api_home, usesModels

urlpatterns = [
    path('', api_home),
    path('model', usesModels)
]
