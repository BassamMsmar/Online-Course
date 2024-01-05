from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import CourseSerializer
from .models import Course


class CousrseListAPI(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CousrseDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer