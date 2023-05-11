from django.db import models
from administrator.models import Question


class Login(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Quiz(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(Login, on_delete=models.CASCADE)



class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
