from django.urls import path
from .api import couser_list_api

urlpatterns = [
    path('api', couser_list_api),
]
