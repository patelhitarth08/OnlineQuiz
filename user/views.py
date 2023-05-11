from administrator.models import Question, Topic
from .forms import LoginForm
from django.contrib import messages
from .models import Login, Quiz, QuizQuestion
from django.shortcuts import render, redirect, HttpResponseRedirect
import random


def register_request(request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            request.session['username'] = request.POST['username']
            messages.success(request, "Registration successful.")
            return redirect("/user")
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
            request.session['userId'] = user.id
            message = "Successfully Logged In"
            return HttpResponseRedirect("user")
        else:
            message = "Invalid Credentials"
    context = {'message': message}
    return render(request=request, template_name="login.html", context=context)


def logout(request):
    request.session.flush()
    return redirect('/user')


def choose_role(request):
    return render(request=request, template_name="chooseRole.html")


def user(request):
    topics = Topic.objects.filter()
    context = {'topics': topics}
    return render(request=request, template_name="user.html", context=context)


def takeQuiz(request, topic_id):

    topic = Topic.objects.filter(id=topic_id).first()
    name = topic.name
    userId = request.session['userId']
    user = Login.objects.get(id=userId)
    user_id = user
    quiz = Quiz(name=name, user=user_id)
    quiz.save()
    questions = Question.objects.filter(topic_id=topic_id)
    question_list = list(questions)
    random.shuffle(question_list)
    random_questions = question_list[:10]

    for question in random_questions:
        question_id = question.id
        quiz_id = quiz.id
        quizQuestion = QuizQuestion(question_id=question_id, quiz_id=quiz_id)
        quizQuestion.save()
    context = {'random_questions': random_questions}
    return render(request=request, template_name="takeQuiz.html", context=context)


def quizSubmit(request):
    questions = request.POST.getlist('random_questions[]')
    score = 0
    result = []
    for question in questions:
        selectedOption = request.POST.get('question' + question, None)

        que = Question.objects.filter(id=question).first()
        att = [que.text, selectedOption, que.answer]
        result.append(att)
        if selectedOption == None:
            continue
        if que.answer == selectedOption:
            score = score + 1
        else:
            score = score - 0.5

    print(result)
    context = {'result': result,
               'total_questions': len(result), 'score': score}
    return render(request=request, template_name="result.html", context=context)

# def selectQuestion(request, question_id):
