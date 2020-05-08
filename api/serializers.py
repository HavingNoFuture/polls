from rest_framework import serializers

from .models import Poll, Question, Session, Answer


class Serializer(serializers.ModelSerializer):
    pass