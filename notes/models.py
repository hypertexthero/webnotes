from django.db import models
from django.db.models import permalink
from markdown import markdown
import datetime
from typogrify.templatetags.typogrify_tags import typogrify

class Note(models.Model):
    
    KIND = (
        ('L', 'Link'),
        ('A', 'Article'),
    )
    
    """Model to save our note"""
    title = models.CharField(max_length=255)
    kind = models.CharField(max_length=1, choices=KIND, default=1, help_text="Is this a link to other content or an original article?")
    # TODO: linkurl field and link/article slug
    url = models.URLField(blank=True, help_text="The link URL")
    # slug = models.SlugField(unique_for_date='pub_date', help_text='Must be unique for the publication date.')
    content_markdown = models.TextField(blank=True, verbose_name='Note (markdown syntax)')
    content_html = models.TextField(editable=False) 
    # created = models.DateTimeField(default=datetime.datetime.now)
    created = models.DateTimeField(default=datetime.datetime.now)
    modified = models.DateTimeField(auto_now_add=True, editable=False)
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
            # typogrify - http://code.google.com/p/typogrify/ and http://djangosnippets.org/snippets/381/
        self.content_html = typogrify(markdown(self.content_markdown, ['footnotes', 'tables', 'nl2br', 'codehilite']))
        # self.content_html = markdown(self.content_markdown)
        self.modified = datetime.datetime.now()
        super(Note, self).save()

    # display note title in admin
    def __unicode__(self):
        return self.title

# 
# 
# class NoteForm(ModelForm):
#     created = DateField(widget=SelectDateWidget)
# 
#     class Meta:
#         model = Note
#         fields = ('title', 'content_markdown', 'created', 'modified')
#         widgets = {
#             'created': SelectDateWidget(),
#             'modified': SelectDateWidget(),
#         }
    
    # define permalink (not needed?)
    # @permalink
    # def get_absolute_url(self):
    #     # return ('collection_detail', None, {'object_id': self.id})
    #     return ("note_permalink", (), {'id': self.id})


# Do I want to do all this just to set the textarea attributes? Or find another way?
# http://stackoverflow.com/questions/4190386/how-to-add-extra-fields-using-django-forms-textarea
# from django.forms import ModelForm, Textarea

# class NoteForm(ModelForm):
#     class Meta:
#         model = Note
#         fields = ('title', 'content_markdown', 'created', 'modified')
#         widgets = {
#             'content_markdown': Textarea(attrs={'cols': 80, 'rows': 40}),
#         }