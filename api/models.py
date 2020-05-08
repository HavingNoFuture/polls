from django.db import models


class PollUser(models.Model):
    cookie = models.CharField("Ключ куки", max_length=150)


QUESTION_TYPE_CHOICES = (
    ('text', 'Ответ текстом'),
    ('one_choice', 'Ответ с выбором одного варианта'),
    ('many_choices', 'Ответ с выбором нескольких вариантов'),
)


class Question(models.Model):
    text = models.TextField("Текст вопроса")
    type = models.CharField("Тип", max_length=100, choices=QUESTION_TYPE_CHOICES, default='text')
    ready_answers = models.TextField("Готовые варианты ответа", default='')


class Poll(models.Model):
    name = models.CharField("Название", max_length=300)
    start_date = models.DateTimeField("Дата старта", auto_now_add=True)
    end_date = models.DateTimeField("Дата окончания")
    description = models.TextField("Описание")
    questions = models.ManyToManyField(Question, verbose_name="Вопросы", related_name="polls")


class Answer(models.Model):
    question = models.ForeignKey(Question, verbose_name="Вопрос", on_delete=models.CASCADE)
    text = models.TextField("Ответ на вопрос")


class Session(models.Model):
    user = models.ForeignKey(PollUser, verbose_name="Пользователь", on_delete=models.CASCADE, related_name="sessions")
    poll = models.ForeignKey(Poll, verbose_name="Опрос", on_delete=models.CASCADE)
    answers = models.ManyToManyField(Answer)
