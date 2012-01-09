from django.db import models
from django.db.models import permalink
from markdown import markdown
import datetime
 
class Notes(models.Model):
    """Model to save our note"""
    title   = models.CharField(max_length=255)
    content_markdown = models.TextField('Entry body')
    content_html = models.TextField(editable=False) 
    created = models.DateTimeField(default=datetime.datetime.now)
    modified = models.DateTimeField(default=datetime.datetime.now)
    #automatically add timestamps when object is created
    # created = models.DateTimeField(auto_now_add=True) 
    #automatically add timestamps when object is updated
    # modified = models.DateTimeField(auto_now=True)

    # display correct plural name in admin
    class Meta:
        ordering = ['modified']
        verbose_name_plural = "notes"

    # TODO: Combine django static generator in ~/django_projects/victoreskinazi.com with the functionality below so we are serving static files in HTML on server and Markdown and HTML columns in database. Also try to find a way to have static files in Markdown format on the server.
    # https://code.djangoproject.com/wiki/UsingMarkup
    def save(self):
        # Also applying codehilite and footnotes markdown extensions: 
            # http://fi.am/entry/code-highlighting-in-django/
            # http://freewisdom.org/projects/python-markdown/CodeHilite
            # http://freewisdom.org/projects/python-markdown/Footnotes
        self.content_html = markdown(self.content_markdown, ['footnotes', 'codehilite']) 
        # self.content_html = markdown(self.content_markdown)
        self.modified = datetime.datetime.now()
        super(Notes, self).save()

    # display note title in admin
    def __unicode__(self):
        return self.title
    
    # define permalink (not needed?)
    # @permalink
    # def get_absolute_url(self):
    #     # return ('collection_detail', None, {'object_id': self.id})
    #     return ("note_permalink", (), {'id': self.id})


# Do I want to do all this just to set the textarea attributes? Or find another way?
# http://stackoverflow.com/questions/4190386/how-to-add-extra-fields-using-django-forms-textarea
# from django.forms import ModelForm, Textarea

# class NotesForm(ModelForm):
#     class Meta:
#         model = Notes
#         fields = ('title', 'content_markdown', 'created', 'modified')
#         widgets = {
#             'content_markdown': Textarea(attrs={'cols': 80, 'rows': 40}),
#         }