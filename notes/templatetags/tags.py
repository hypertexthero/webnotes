# http://www.djangrrl.com/post/custom-template-tags-in-django/

from webnotes.notes.models import Notes
from django import template

register = template.Library()

def latestnote():
    notes = Notes.objects.all().order_by('-last_update', 'title')[:1]
    return {'notes': notes}

register.inclusion_tag('includes/last_updated_note.html')(latestnote)
