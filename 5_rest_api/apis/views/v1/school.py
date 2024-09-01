from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from ...models import School, Student, Teacher
from ...serializers import SchoolSerializer
from ...filters import SchoolFilter

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = SchoolFilter
    search_fields = ('name',)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        response = super().retrieve(request, *args, **kwargs)
        response.data['classroom_count'] = instance.classrooms.count()
        response.data['teacher_count'] = Teacher.objects.filter(classrooms__school=instance).distinct().count()
        response.data['student_count'] = Student.objects.filter(classroom__school=instance).count()
        return response
