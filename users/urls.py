from django.urls import path
from . import views
urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("account/", views.user_account, name="account"),
    path("register/", views.registerUser, name="register"),
    path("edit-account/", views.edit_account, name="edit-account"),
    path('logout/', views.logoutUser, name="logout"),
    path("", views.profile, name="profile"),
    path("profile/<str:pk>", views.user_profile, name="user-profile",),
]