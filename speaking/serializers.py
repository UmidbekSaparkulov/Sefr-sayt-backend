from rest_framework import serializers
from .models import TestInfo, TestTip, Expectation, SampleQuestion, SampleQuestionGuideline

# 1️⃣ TestInfo serializer
class TestInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestInfo
        fields = "__all__"

# 2️⃣ TestTip serializer
class TestTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestTip
        fields = "__all__"

# 3️⃣ Expectation serializer
class ExpectationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expectation
        fields = "__all__"

# 4️⃣ SampleQuestionGuideline serializer
class SampleQuestionGuidelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleQuestionGuideline
        fields = "__all__"

# 5️⃣ SampleQuestion serializer, ichida guidelines
class SampleQuestionSerializer(serializers.ModelSerializer):
    guidelines = SampleQuestionGuidelineSerializer(many=True, read_only=True)

    class Meta:
        model = SampleQuestion
        fields = "__all__"
