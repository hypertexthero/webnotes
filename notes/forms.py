from django import forms
from django.forms import extras
from django.forms import ModelForm

from models import Notes

# Using ModelForm here to override the model's default text input widget and have a drop down menu with selectable date (and soon, time). Also need to specify form_class=NotesForm in the create_object generic views function in views.py

class NotesForm(ModelForm): 
    created = forms.DateField(widget=extras.SelectDateWidget) 
    modified = forms.DateField(widget=extras.SelectDateWidget) 
    class Meta:
        model = Notes 
        # exclude = ['created', 'modified']
        # widgets = {
        #     'created': SelectDateWidget(),
        #     'modified': SelectDateWidget(),
        # }