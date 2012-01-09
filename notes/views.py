from django.views.generic.list_detail import object_list
from django.views.generic.list_detail import object_detail
from django.views.generic.create_update import create_object
from django.views.generic.create_update import update_object
from django.views.generic.create_update import delete_object
from django.contrib.auth.decorators import login_required # for @login_required decorator
from django.core.urlresolvers import reverse
 
from models import Notes

# def login_view(request):
#     if request.method == 'POST':
#         user = authenticate(username = request.POST['login_username'], password = request.POST['login_password'])
#         if user is None:
#             return direct_to_template(request, 'invalid_login.html')
#             if not user.is_active:
#                 return direct_to_template(request, 'inactive_account.html')
#                 login(request, user)
#                 try:
#                     return HttpResponseRedirect(request.META.get('HTTP_REFERER', None))
#                 except KeyError:
#                     return HttpResponseRedirect('/')
# 
# def logout_view(request):
#     logout(request)
#     try:
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER', None))
#     except KeyError:
#         return HttpResponseRedirect('/')
 
def notes_list(request):
    """Show all notes"""
 
    return object_list(request, 
        queryset=Notes.objects.all().order_by('-modified', 'title'), # https://docs.djangoproject.com/en/dev/ref/models/querysets/#django.db.models.query.QuerySet.order_by
        template_name='notes/list.html',
        template_object_name='note'
    )
 
def notes_detail(request, id):
    """View note detail based on note id"""

    return object_detail(request,
        queryset=Notes.objects.all(),
        object_id=id,
        template_name='notes/detail.html',
        template_object_name='note'
    )

# see also this alternative: http://djangosnippets.org/snippets/966/
@login_required
def notes_create(request):
    """Create new note"""
 
    return create_object(request,
        model=Notes,
        template_name='notes/create.html',
        post_save_redirect=reverse("notes_list")
    )            

@login_required
def notes_update(request, id):
    """Update note based on id"""
 
    return update_object(request,
        model=Notes,
        object_id=id,
        template_name='notes/update.html',
        post_save_redirect=reverse("notes_list")
    )            

@login_required
def notes_delete(request, id):
    """Delete a note based on id"""
    
    return delete_object(request,
        model=Notes,
        object_id=id,
        template_object_name='note',
        template_name='notes/delete.html',
        post_delete_redirect=reverse("notes_list")
    )