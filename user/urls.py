from django.urls import path
from . import views
app_name = "user"

urlpatterns = [
    path("register", views.register_request, name="register"),
    path("", views.choose_role, name="choose_role"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout, name='logout'),
    path("takeQuiz/<int:topic_id>", views.takeQuiz, name='takeQuiz'),
    path("quizSubmit/", views.quizSubmit, name="quizSubmit"),
    path("user", views.user, name="user"),
]
