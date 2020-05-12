from datetime import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions, viewsets, generics
from .models import Poll, Question, PollUser, Session, Answer
from . import serializers


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.filter(end_date__gt=datetime.today()).order_by('end_date')
    serializer_class = serializers.PollSerializer
    permission_classes = (permissions.IsAdminUser,)

    def get_permissions(self):
        if self.action == 'list':
            return (permissions.AllowAny(),)
        return super().get_permissions()


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = (permissions.IsAdminUser,)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PollUser.objects.all()
    serializer_class = serializers.PollUserSerializer


class SessionsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Session.objects.all()
    serializer_class = serializers.SessionSerializer

    def get_queryset(self):
        queryset = Session.objects.filter(poll__id=self.kwargs.get('poll_id'))
        return queryset


class AnswerViewSet(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = serializers.CreateAnswerSerializer

    def create(self, request, *args, **kwargs):
        questions = Poll.objects.get(id=self.kwargs.get('poll_id')).questions.all()
        question_ids = questions.values_list('id', flat=True).order_by("id")
        if self.kwargs.get('question_id') not in question_ids:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        cookie = self.request.session.get("POLL_USER_COOKIE", None)
        if not cookie:
            new_user = PollUser.objects.create()
            cookie = str(new_user.id)
            self.request.session["POLL_USER_COOKIE"] = cookie

        user = PollUser.objects.get(id=cookie)
        session, _ = Session.objects.get_or_create(user_id=user.id, poll_id=self.kwargs.get('poll_id'))
        answer = serializer.save(question_id=self.kwargs.get('question_id'))
        session.answers.add(answer)
        session.save()
