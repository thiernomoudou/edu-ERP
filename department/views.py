from django.shortcuts import render

from .models import ClassLevel, Department, Program
from .serializers import ClassLevelSerializer, DepartmentSerializer, ProgramSerializer
from .permissions import IsAccountOwner

from rest_framework import viewsets, permissions




class ClassLevelViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = ClassLevel.objects.all()
    serializer_class = ClassLevelSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

