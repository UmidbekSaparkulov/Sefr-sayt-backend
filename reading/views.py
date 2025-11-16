from rest_framework import viewsets
from .models import ReadingTest, Option, Question, Segment, Paragraph, Heading
from .serializers import (
    ReadingTestSerializer,
    OptionSerializer,
    QuestionSerializer,
    SegmentSerializer,
    ParagraphSerializer,
    HeadingSerializer
)

class ReadingTestViewSet(viewsets.ModelViewSet):
    queryset = ReadingTest.objects.all()
    serializer_class = ReadingTestSerializer

class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class SegmentViewSet(viewsets.ModelViewSet):
    queryset = Segment.objects.all()
    serializer_class = SegmentSerializer

class ParagraphViewSet(viewsets.ModelViewSet):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer

class HeadingViewSet(viewsets.ModelViewSet):
    queryset = Heading.objects.all()
    serializer_class = HeadingSerializer
