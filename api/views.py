from datetime import datetime

from rest_framework import permissions, viewsets
from .models import Poll, Question, PollUser, Session
from .serializers import PollSerializer, QuestionSerializer, PollUserSerializer, SessionSerializer


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.filter(end_date__gt=datetime.today()).order_by('end_date')
    serializer_class = PollSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get_permissions(self):
        if self.action == 'list':
            return (permissions.AllowAny(),)
        return super().get_permissions()


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAdminUser,)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PollUser.objects.all()
    serializer_class = PollUserSerializer


class SessionsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def get_queryset(self):
        queryset = Session.objects.filter(poll__id=self.kwargs.get('poll_id'))
        return queryset
