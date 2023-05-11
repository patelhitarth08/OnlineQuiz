from django.http import JsonResponse
from .forms import LoginForm, QuestionForm, TopicForm
from django.contrib import messages
from .models import Login, Question, Topic
from django.shortcuts import get_object_or_404, render, redirect, HttpResponseRedirect
import random


def register_request(request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            request.session['username'] = request.POST['username']
            messages.success(request, "Registration successful.")
            return redirect("/administrator/login")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
        message = "Unsuccessful registration. Invalid information."
    form = LoginForm()
    return render(request=request, template_name="register.html", context={"register_form": form, 'message': message})


def login_request(request):
    message = ""
    if request.method == "POST":
        password = request.POST['password']
        username = request.POST['username']
        user = Login.objects.filter(username=username).first()
        if user is not None and user.password == password:
            request.session['username'] = username
            request.session['id'] = user.id
            print(user.id)
            return HttpResponseRedirect("admin")
        else:
            message = "Invalid Credentials"
    context = {'message': message}
    return render(request=request, template_name="login.html", context=context)


def logout(request):
    request.session.flush()
    return redirect('/administrator')


def add_topic(request):
    form = TopicForm(request.POST)
    if form.is_valid():
        topic = form.save(commit=False)
        # set admin_id to logged in user's Login object
        adminId = request.session['id']
        user = Login.objects.get(id=adminId)
        topic.admin_id = user
        topic.save()
        return redirect('/administrator/admin')
    else:
        form = TopicForm()
    return render(request=request, template_name="addTopic.html", context={'form': form})


def viewQuestion(request, topic_id):
    questions = Question.objects.filter(topic_id=topic_id)
    context = {'questions': questions}
    return render(request=request, template_name="viewQuestion.html", context=context)


def addQuestion(request, topic_id):
    form = QuestionForm(request.POST)
    if form.is_valid():
        question = form.save(commit=False)

        topic = Topic.objects.get(id=topic_id)
        topic.total_questions = topic.total_questions + 1
        topic.save()
        # set admin_id to logged in user's Login object
        text = request.POST['text']
        option1 = request.POST['option1']
        option2 = request.POST['option2']
        option3 = request.POST['option3']
        option4 = request.POST['option4']
        correctOption = request.POST['correctOption']
        question = Question(text=text, option1=option1,
                            option2=option2, option3=option3, option4=option4, topic_id=topic_id, correctOption=correctOption)

        if correctOption == "option1":
            question.answer = option1
        elif correctOption == "option2":
            question.answer = option2
        elif correctOption == "option3":
            question.answer = option3
        else:
            question.answer = option4

        question.save()
        return redirect('/administrator/addQuestion/' + str(topic_id))
    else:
        form = QuestionForm()
    return render(request=request, template_name="addQuestion.html", context={'form': form})


def home(request):
    topics = Topic.objects.filter(admin_id_id=request.session['id'])
    context = {'topics': topics}
    return render(request=request, template_name="admin.html", context=context)


def choose_role(request):
    return render(request=request, template_name="chooseRole.html")
