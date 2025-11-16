from rest_framework import serializers
from .models import ReadingTest, Option, Question, Segment, Paragraph, Heading

# Option serializer
class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

# Question serializer, ichida options bo‘ladi
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

# Segment serializer
class SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segment
        fields = '__all__'

# Paragraph serializer
class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = '__all__'

# Heading serializer
class HeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heading
        fields = '__all__'

# ReadingTest serializer, ichida nested objects
class ReadingTestSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    questions = QuestionSerializer(many=True, read_only=True)
    segments = SegmentSerializer(many=True, read_only=True)
    paragraphs = ParagraphSerializer(many=True, read_only=True)
    headings = HeadingSerializer(many=True, read_only=True)

    class Meta:
        model = ReadingTest
        fields = '__all__'
