from django.urls import path
from . import views

urlpatterns = [
    path("register", views.Register.as_view()),
    path("login", views.Login.as_view()),
    path("user", views.UserView.as_view()),
    path("logout", views.Logout.as_view()),
    path("getAllMemberUsers", views.GetAllMemberUsersView.as_view()),
    path("deleteMyOwnAccount", views.DeleteAccount.as_view()),
    path("deleteMemberAccount/<str:id>", views.DeleteMemberAccount.as_view()),
]
