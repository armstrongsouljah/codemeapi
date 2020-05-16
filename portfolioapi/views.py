from django.shortcuts import render
from rest_framework import generics as g 
from .serializers import ProjectSerializer
from .models import Project
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)


class ProjectListView(g.ListAPIView):
    queryset = Project.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = ProjectSerializer


class ProjectAddView(g.CreateAPIView):
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated, ]
    serializer_class = ProjectSerializer

