from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("project/<str:pk>", views.project, name="project"),
    path("test/", views.test, name="test")
]