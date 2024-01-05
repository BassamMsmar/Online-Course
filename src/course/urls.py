from django.urls import path
from .api import CousrseListAPI, CousrseDetailAPI

urlpatterns = [
    path('api', CousrseListAPI.as_view()),
    path('api/<int:pk>', CousrseDetailAPI.as_view()),
]
