from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from ...models import Teacher
from ...serializers import TeacherSerializer
from ...filters import TeacherFilter

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = TeacherFilter

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        response = super().retrieve(request, *args, **kwargs)
        response.data['classroom_list'] = [classroom.id for classroom in instance.classrooms.all()]
        return response
