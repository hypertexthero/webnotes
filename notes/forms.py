from django import forms
from django.forms import ModelForm
import datetime

from models import Notes
from widgets import SplitSelectDateTimeWidget
from webnotes import settings

# Using ModelForm here to override the model's default text input widget and have a drop down menu with selectable date (and soon, time). Also need to specify form_class=NotesForm in the create_object generic views function in views.py

class NotesForm(ModelForm): 
    created = forms.DateTimeField(
        widget = SplitSelectDateTimeWidget(
            years=range(1978, datetime.date.today().year+10) # The years argument was necessary to specify a range of selectable years - http://stackoverflow.com/questions/3232364/display-a-series-of-dropdown-lists-with-past-dates-in-django
            ), 
        initial = datetime.datetime.now()
    )
    # modified = forms.DateTimeField(widget=SplitSelectDateTimeWidget(twelve_hr=False)) 
    class Meta:
        model = Notes 