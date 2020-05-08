from datetime import datetime

from rest_framework import permissions, viewsets
from .models import Poll, Session
from .serializers import Serializer


# class PollViewSet(viewsets.ModelViewSet):
#     queryset = Poll.object.filter(end_date__gt=datetime.today())
#     serializer_class = Serializer
#
# class SessionViewSet(viewsets.ModelViewSet):
#     queryset = Session.object.all()
#     serializer_class = Serializer
