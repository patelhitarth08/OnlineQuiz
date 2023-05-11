from django.urls import path
from . import views
app_name = "administrator"

urlpatterns = [
    path("register", views.register_request, name="register"),
    path("", views.choose_role, name="chooseRole"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout, name='logout'),
    path("addTopic", views.add_topic, name='add_topic'),
    path("addQuestion/<int:topic_id>/", views.addQuestion, name='addQuestion'),
    path("viewQuestion/<int:topic_id>/",
         views.viewQuestion, name='viewQuestion'),
    path("admin", views.home, name="admin"),
]
