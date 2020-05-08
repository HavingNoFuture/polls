from datetime import datetime

from rest_framework import permissions, viewsets
from .models import Poll, Session, Question
from .serializers import PollSerializer, QuestionSerializer


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.filter(end_date__gt=datetime.today())
    serializer_class = PollSerializer


# class SessionViewSet(viewsets.ModelViewSet):
#     queryset = Session.object.all()
#     serializer_class = Serializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
