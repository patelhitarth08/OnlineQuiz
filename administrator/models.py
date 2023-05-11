
from django.db import models


class Login(models.Model):
    username = models.CharField(max_length=255, unique=True, blank=False)
    password = models.CharField(max_length=255, blank=False)


class Topic(models.Model):
    name = models.CharField(max_length=255)
    admin_id = models.ForeignKey(Login, on_delete=models.CASCADE)
    total_questions = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.admin_id_id:
            # set admin_id to logged in user's Login object
            self.admin_id_id = get_current_user_login_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


ANSWER = (
    ('option1', 'option1'),
    ('option2', 'option2'),
    ('option3', 'option3'),
    ('option4', 'option4')
)


class Question(models.Model):
    text = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    correctOption = models.CharField(max_length=max(
        len(v[0]) for v in ANSWER), choices=ANSWER, blank=False, default="option1")
    answer = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)


def get_current_user_login_id():
    return Login.objects.filter(username=Login.username).first().id
