from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from ...models import Classroom
from ...serializers import ClassroomSerializer
from ...filters import ClassroomFilter

class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = ClassroomFilter

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        response = super().retrieve(request, *args, **kwargs)
        response.data['teacher_list'] = [teacher.id for teacher in instance.teachers.all()]
        response.data['student_list'] = [student.id for student in instance.students.all()]
        return response
