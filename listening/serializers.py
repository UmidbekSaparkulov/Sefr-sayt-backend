from rest_framework import serializers
from .models import ListeningTest, ListeningQuestion, ListeningOption

# Option serializer
class ListeningOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListeningOption
        fields = '__all__'

# Question serializer, ichida options
class ListeningQuestionSerializer(serializers.ModelSerializer):
    options = ListeningOptionSerializer(many=True, read_only=True)

    class Meta:
        model = ListeningQuestion
        fields = '__all__'

# Test serializer, ichida questions
class ListeningTestSerializer(serializers.ModelSerializer):
    questions = ListeningQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = ListeningTest
        fields = '__all__'
