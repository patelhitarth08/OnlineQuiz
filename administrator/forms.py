from django import forms
from .models import Login, Topic, Question


class LoginForm(forms.ModelForm):

    class Meta:
        model = Login
        fields = "__all__"


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['name']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'option1', 'option2',
                  'option3', 'option4', 'correctOption']
