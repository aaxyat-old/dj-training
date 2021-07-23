from django.db import models
from uuid import uuid4
from users.models import Profile


# Create your models here.


class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True, max_length=10000)
    featured_image = models.ImageField(null=True,blank=True, default="pattern.jpg")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0,null=True, blank=True)
    vote_ratio = models.IntegerField(default=0,null=True, blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    vote_type = (
        ("up", "Up Vote"),
        ("down", "Down Vote"),
    )
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)
    #owner =
    project = models.ForeignKey(Project, on_delete=models.CASCADE,)
    body = models.TextField(blank=True, null=True, max_length=10000)
    value = models.CharField(max_length=255, choices=vote_type)

    def __str__(self):
        return self.project.title


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
