from django.views.generic.date_based import archive_index

from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from django.views.generic.create_update import create_object
from django.views.generic.create_update import update_object
from django.views.generic.create_update import delete_object
from django.contrib.auth.decorators import login_required # for @login_required decorator
from django.core.urlresolvers import reverse
 
from models import Note
from forms import NoteForm

# generic archive_index view to display notes ordered by date and not display ones saved with a future date - https://docs.djangoproject.com/en/dev/ref/generic-views/#django-views-generic-date-based-archive-index
def notes_list(request): 
    """Show all notes"""
    
    return archive_index(request, 
        queryset=Note.objects.all().order_by('-created', 'title'), # https://docs.djangoproject.com/en/dev/ref/models/querysets/#django.db.models.query.QuerySet.order_by
        date_field='created', # don't forget to set {{ note.created|date:"d F Y" }} in notes/list.html
        template_name='notes/list.html',
        # template_object_name='note',
        allow_future = False # this is the default, but am keeping it here to remember that it can be set to true for other use cases, such as calendar of upcoming events
    )

def notes_archive(request): 
    """Archive of all notes"""

    return archive_index(request, 
        queryset=Note.objects.all().order_by('-created', 'title'), # https://docs.djangoproject.com/en/dev/ref/models/querysets/#django.db.models.query.QuerySet.order_by
        date_field='created', # don't forget to set {{ note.created|date:"d F Y" }} in notes/list.html
        template_name='notes/archive.html',
        # template_object_name='note',
        allow_future = False # this is the default, but am keeping it here to remember that it can be set to true for other use cases, such as calendar of upcoming events
    )

# def notes_list(request):
#     """Show all notes"""
#     
#     return object_list(request, 
#         queryset=Note.objects.all().order_by('-modified', 'title'), # https://docs.djangoproject.com/en/dev/ref/models/querysets/#django.db.models.query.QuerySet.order_by
#         template_name='notes/list.html',
#         template_object_name='note'
#     )
 
def notes_detail(request, id):
    """View note detail based on note id"""

    return object_detail(request,
        queryset=Note.objects.all(),
        object_id=id,
        template_name='notes/detail.html',
        template_object_name='note' # so I can write {{ note.title }} in templates/notes/detail.html (otherwise I would need to write {{ object.title }})
    )

# see also this alternative: http://djangosnippets.org/snippets/966/
@login_required
def notes_create(request):
    """Create new note"""
 
    return create_object(request,
        # model=Note
        form_class=NoteForm, # Needed to specify form_class instead of model so that the custom date widget for dropdown menu is displayed: https://docs.djangoproject.com/en/dev/ref/generic-views/#django-views-generic-create-update-create-object
        # extra_context={'kind': 'kind', 'url': 'url'},
        template_name='notes/create.html',
        # post_save_redirect=reverse("notes_list")
        post_save_redirect="/notes/archive/%(id)s/" # todo: add object.get_absolute_url() to models.py
    )            

@login_required
def notes_update(request, id):
    """Update note based on id"""
 
    return update_object(request,
        # model=Note
        form_class=NoteForm, # Needed to specify form_class instead of model so that the custom date widget for dropdown menu is displayed: https://docs.djangoproject.com/en/dev/ref/generic-views/#django-views-generic-create-update-create-object
        object_id=id,
        template_name='notes/update.html',
        # extra_context={'kind': 'kind', 'url': 'url'},
        post_save_redirect="/notes/archive/%(id)s/", # todo: add object.get_absolute_url() to models.py
        template_object_name='note' # so I can write {{ note.title }} in templates/notes/update.html (otherwise I would need to write {{ object.title }})
    )            

@login_required
def notes_delete(request, id):
    """Delete a note based on id"""
    
    return delete_object(request,
        model=Note,
        object_id=id,
        template_object_name='note', # so I can write {{ note.title }} in templates/notes/delete.html (otherwise I would need to write {{ object.title }})
        template_name='notes/delete.html',
        post_delete_redirect=reverse("notes_list")
    )

# =Search

# from django.http import HttpResponse 
# from django.template import loader, Context
# 
# def search(request): 
#     query = request.GET['q']
#     results = Note.objects.filter(content_html__icontains=query)
#     template = loader.get_template('notes/search.html')
#     context = Context({ 'query': query, 'results': results })
#     response = template.render(context)
#     return HttpResponse(response)

# or use django's render_to_response shortcut:

from django.shortcuts import render_to_response
from django.db.models import Q

# def search(request):
#     query = request.GET['q']
#     return render_to_response('notes/search.html',
#         {   'query': query, 
#             'results': Note.objects.filter(content_html__icontains=query) })

# rewritten so /search/ URL can be accessed directly:

def search(request):    
    query = request.GET.get('q', '') # both /search/ and /search/?q=query work
    results = []
    # http://stackoverflow.com/a/4338108/412329 - passing the user variable into the context
    user = request.user
    if query:
        # INSTEAD OF THIS:
        # title_results = Note.objects.filter(title__icontains=query)
        # results = Note.objects.filter(content_html__icontains=query)
        # DO THIS avoid duplicate results when query word is both in title and content_html:
        # http://stackoverflow.com/questions/744424/django-models-how-to-filter-out-duplicate-values-by-pk-after-the-fact
        results = Note.objects.filter(Q(title__icontains=query)|Q(content_html__icontains=query)).distinct()
    return render_to_response('notes/search.html',
        {   'query': query, 
            'results': results,
            'user': user
             })