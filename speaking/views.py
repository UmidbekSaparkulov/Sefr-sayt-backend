from rest_framework import viewsets
from .models import TestInfo, TestTip, Expectation, SampleQuestion, SampleQuestionGuideline
from .serializers import (
    TestInfoSerializer,
    TestTipSerializer,
    ExpectationSerializer,
    SampleQuestionSerializer,
    SampleQuestionGuidelineSerializer
)

class TestInfoViewSet(viewsets.ModelViewSet):
    queryset = TestInfo.objects.all()
    serializer_class = TestInfoSerializer

class TestTipViewSet(viewsets.ModelViewSet):
    queryset = TestTip.objects.all()
    serializer_class = TestTipSerializer

class ExpectationViewSet(viewsets.ModelViewSet):
    queryset = Expectation.objects.all()
    serializer_class = ExpectationSerializer

class SampleQuestionViewSet(viewsets.ModelViewSet):
    queryset = SampleQuestion.objects.all()
    serializer_class = SampleQuestionSerializer

class SampleQuestionGuidelineViewSet(viewsets.ModelViewSet):
    queryset = SampleQuestionGuideline.objects.all()
    serializer_class = SampleQuestionGuidelineSerializer
