from django.shortcuts import render
from .models import Project

# Create your views here.
projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]


def index(request):
    context = {
        "projects": projectsList
    }

    return render(request,"projects/index.html", context)


def project(request, pk):
    search = None
    for item in projectsList:
        if item["id"] == pk:
            search = item

    return render(request, "projects/project.html", context={"search":search})

def test(request):
    data = Project.objects.all().values()
    return render(request, "projects/test.html",{"data":data})
