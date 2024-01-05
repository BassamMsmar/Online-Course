from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CourseListSerializer, CourseDetailSerializer


from .models import Course


class CousrseListAPI(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['category']
    ordering_fields = ['name', 'category']
    search_fields = ['name', 'description', 'description, price']


class CousrseDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer