from rest_framework import serializers

from .models import Poll, Question, Session, Answer


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('text', 'type')


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(read_only=True, many=True)

    class Meta:
        model = Poll
        fields = ('name', 'description', 'questions')

