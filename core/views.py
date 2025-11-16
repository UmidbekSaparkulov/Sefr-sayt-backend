from rest_framework import viewsets
from django.shortcuts import render
from .serializers import LevelSerializer, SkillSerializer
from .models import Level, Skill
# Create your views here.

class CoreLevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class CoreSkillSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer