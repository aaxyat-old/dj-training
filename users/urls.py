from django.urls import path
from . import views
urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path("", views.profile, name="profile"),
    path("profile/<str:pk>", views.user_profile, name="user-profile",),
]