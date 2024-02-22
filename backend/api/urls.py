from django.urls import path
from .views import api_home, usesModels, drf_view

urlpatterns = [
    path('', api_home),
    path('model', usesModels),
    path('drf_model', drf_view)
]
