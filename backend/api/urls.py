from django.urls import path
from .views import api_home, usesModels, drf_view, drf_post_view

urlpatterns = [
    path('', api_home),
    path('model', usesModels),
    path('drf_model', drf_view),
    path('drf_model_post', drf_post_view)
]
