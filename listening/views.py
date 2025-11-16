from rest_framework import viewsets
from .models import ListeningTest, ListeningQuestion, ListeningOption
from .serializers import ListeningTestSerializer, ListeningQuestionSerializer, ListeningOptionSerializer

class ListeningTestViewSet(viewsets.ModelViewSet):
    queryset = ListeningTest.objects.all()
    serializer_class = ListeningTestSerializer

class ListeningQuestionViewSet(viewsets.ModelViewSet):
    queryset = ListeningQuestion.objects.all()
    serializer_class = ListeningQuestionSerializer

class ListeningOptionViewSet(viewsets.ModelViewSet):
    queryset = ListeningOption.objects.all()
    serializer_class = ListeningOptionSerializer
