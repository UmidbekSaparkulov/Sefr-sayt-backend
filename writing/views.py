from rest_framework import viewsets
from .models import Writing
from .serializers import WritingSerializer

class WritingViewSet(viewsets.ModelViewSet):
    queryset = Writing.objects.all()
    serializer_class = WritingSerializer

