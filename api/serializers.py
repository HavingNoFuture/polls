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


class ReadAnswerSerializer(serializers.ModelSerializer):
    question = serializers.SlugRelatedField(slug_field='text', read_only=True)

    class Meta:
        model = Answer
        fields = ('question', 'text')


class CreateAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('text',)


class SessionSerializer(serializers.ModelSerializer):
    poll = serializers.SlugRelatedField(slug_field='name', read_only=True,)
    answers = ReadAnswerSerializer(many=True)

    class Meta:
        model = Session
        fields = ('poll', 'answers')


class PollUserSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True)

    class Meta:
        model = PollUser
        fields = ('sessions',)
