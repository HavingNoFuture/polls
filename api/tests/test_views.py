from datetime import datetime

from django.test import TestCase
from rest_framework import status
from api.models import Question, Poll, Answer

from api import serializers

def get_fixtures():
    q1 = Question.objects.create(type="text", text="Question 1?")
    q2 = Question.objects.create(type="text", text="Question 2?")
    q3 = Question.objects.create(type="text", text="Question 3?")
    q4 = Question.objects.create(type="text", text="Question 4?")
    poll1 = Poll.objects.create(name="Poll 1", start_date="2020-05-08 17:41:28", end_date="2020-12-12 17:41:28",
                        description="desc 1")
    poll1.questions.add(q1, q2, q3, q4)
    poll1.save()
    p2 = Poll.objects.create(name="Poll 2", start_date="2020-05-07 20:41:28", end_date="2020-05-09 12:41:28",
                        description="desc 2")
    p2.questions.add(q1, q2)
    p2.save()
    Answer.objects.create(question=q1, text="text 1")
    Answer.objects.create(question=q2, text="text 2")
    Answer.objects.create(question=q3, text="text 3")
    Answer.objects.create(question=q4, text="text 4")
    Answer.objects.create(question=q1, text="text 5")


class PollViewSetTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        get_fixtures()

    def test_list_poll_viewset(self):
        response = self.client.get('/api/v1/polls/')
        polls = Poll.objects.filter(end_date__gt=datetime.today()).order_by('end_date')
        serializer = serializers.PollSerializer(polls, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_poll_viewset(self):
        response_1 = self.client.get('/api/v1/polls/1/')
        self.assertEqual(response_1.status_code, status.HTTP_403_FORBIDDEN)
        poll_1 = Poll.objects.get(id=1)
        serializer = serializers.PollSerializer(poll_1)
        # print(response_1.data)
        # print(serializer.data)
        # self.assertEqual(response_1.data, serializer.data)
        # self.assertEqual(response_1.status_code, status.HTTP_200_OK)

    def test_2(self):
        response_2 = self.client.get('/api/v1/polls/2/')
        poll_2 = Poll.objects.get(id=2)
        serializer = serializers.PollSerializer(poll_2)
        self.assertEqual(response_2.data, serializer.data)
        self.assertEqual(response_2.status_code, status.HTTP_200_OK)

