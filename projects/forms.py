from django.forms import ModelForm
from django import forms

from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title',"description","featured_image","tags","demo_link","source_link"]
        widgets = {
            'tags':forms.CheckboxSelectMultiple
        }

    def __init__(self,*args,**kwargs):
        super(ProjectForm, self).__init__(*args,**kwargs)
        # self.fields['title'].widget.attrs.update({"class":"input", 'placeholder':"Add Title"})
        for i in self.fields:
            self.fields[f'{i}'].widget.attrs.update({"class": "input", 'placeholder': "Add Title"})