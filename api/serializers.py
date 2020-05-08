from rest_framework import serializers

from .models import Poll, Question, Session, Answer, PollUser


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('text', 'type', 'ready_answers')


class PollSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(read_only=True, many=True)

    class Meta:
        model = Poll
        fields = ('name', 'description', 'questions')


class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.SlugRelatedField(slug_field='text', read_only=True,)

    class Meta:
        model = Answer
        fields = ('question', 'text')


class SessionSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    poll = serializers.SlugRelatedField(slug_field='name', read_only=True,)
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Poll
        fields = ('user', 'poll', 'answers')


class PollUserSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True)

    class Meta:
        model = PollUser
        fields = ('sessions',)
