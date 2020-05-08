from datetime import datetime

from rest_framework import permissions, viewsets
from .models import Poll, Question, PollUser
from .serializers import PollSerializer, QuestionSerializer, PollUserSerializer


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.filter(end_date__gt=datetime.today())
    serializer_class = PollSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get_permissions(self):
        if self.action == 'list':
            return permissions.AllowAny()


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAdminUser,)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PollUser.objects.all()
    serializer_class = PollUserSerializer
