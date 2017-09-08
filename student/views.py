from django.shortcuts import render

from .models import Student, Baccalaureat, Country, StudentDetail
from .serializers import StudentSerializer, BaccalaureatSerializer, CountrySerializer, StudentDetailSerializer
from .permissions import IsAccountOwner

from rest_framework import viewsets, permissions




class StudentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class BaccalaureatViewSet(viewsets.ModelViewSet):
    queryset = Baccalaureat.objects.all()
    serializer_class = BaccalaureatSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class StudentDetailViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = StudentDetail.objects.all()
    serializer_class = StudentDetailSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)