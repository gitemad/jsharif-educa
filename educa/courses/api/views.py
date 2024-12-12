from rest_framework import generics
from courses.models import Subject, Course
from .serializers import SubjectSerializer, CourseListSerializer, CourseDetailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .permissions import IsEnrolled
# from rest_framework.decorators import action

# class SubjectListView(generics.ListAPIView):
#     queryset = Subject.objects.all()
#     serializer_class = SubjectSerializer

# class SubjectDetailView(generics.RetrieveAPIView):
#     queryset = Subject.objects.all()
#     serializer_class = SubjectSerializer

class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer

class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    permission_classes = [IsEnrolled]

class CourseEnrollView(APIView):
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        course = get_object_or_404(
            Course,
            pk=pk
        )
        course.students.add(request.user)

        return Response({
            'enrolled': True,
        })

class SubjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    # @action(detail=True, methods=['post'])
    # def delete(self, request, *args, **kwargs):
    #     pass