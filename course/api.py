from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CourseSerializer
from .models import Course

@api_view()
def couser_list_api(request):
    courses = Course.objects.all()
    data = CourseSerializer(courses, many=True).data
    return Response(data)