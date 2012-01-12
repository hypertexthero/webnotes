# Create home for your code

(Lines starting with the dollar sign $ signify a command that you run in a Terminal)

    $ cd ~ 
    $ mkdir code
    $ cd code

# Install programming language (Python)

Install python: <http://www.python.org/getit/>

# Install tool for creating isolated Python development environments (virtualenv) and tool for installing and managing Python packages (pip)

<http://www.pip-installer.org/en/latest/installing.html>

The recommended way to use pip is within virtualenv, since every virtualenv has pip installed in it automatically. This does not require root access or modify your system Python installation. For instance: i.e. Download the following file and put it in your code folder: https://raw.github.com/pypa/virtualenv/master/virtualenv.py

    $ curl -O https://raw.github.com/pypa/virtualenv/master/virtualenv.py
    $ python virtualenv.py my_new_env
    $ . my_new_env/bin/activate
    (my_new_env)$ pip install ...

When used in this manner, pip will only affect the active virtual environment. If you do want to install pip globally into your Python installation, see the instructions below.

    $ virtualenv --no-site-packages webnotes-env
    $ cd webnotes-env
    $ . bin/activate

# Install web framework and a very useful data/schema migration tool (Django and South)

    $ pip install django
    $ pip install south

# Start new project with Django

    $ django-admin.py startproject webnotes

# Setup development database settings - edit inside settings.py (webnotes/settings.py) - we are using sqlite3, which should already be available since it is included with Python

    DATABASE_ENGINE = 'sqlite3' 
    DATABASE_NAME = 'webnotes.db'

# Create templates folder #

    $ cd webnotes
    $ mkdir templates

# Download the base.html file and the 'notes' folder from the following URL and put them inside webnotes/templates

<https://github.com/gchandrasa/django-tutorial-webnotes/tree/master/webnotes/templates>

The directory structure should look like this:

    webnotes
        - templates
            - base.html
            - notes
                - create.html
                - delete.html
                - detail.html
                - list.html
                - update.html

# Edit/add inside settings.py (so your project knows where to find templates)

    import os
    PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

    TEMPLATE_DIRS = (
        os.path.join(PROJECT_ROOT, 'templates')
    )

# Add South to the INSTALLED_APPS lists in settings.py

    ...
    INSTALLED_APPS = (
        ...
        ‘south’,
    )
    ...

# Run ‘syncdb’ to create your initial database tables provided by django such as auth, etc (before you create your own models - this is the last time you’ll run ‘syncdb’)

Follow the instructions after running the command.

    $ python manage.py syncdb

# Run first data migration

## Create a new app and create your initial ‘models.py’ file for it (start new app with Django)

    $ django-admin.py startapp notes

## Create your models - put in models.py (webnotes/notes/models.py) #

    from django.db import models

    class Notes(models.Model):
        """Model to save our note"""
        title   = models.CharField(max_length=255)
        content = models.TextField()
        #automatically add timestamps when object is created 
        added_at = models.DateTimeField(auto_now_add=True) 
        #automatically add timestamps when object is updated
        last_update = models.DateTimeField(auto_now=True) #

## Add your app to your created app to INSTALLED_APPS (south should always be last?) #

    ...
    INSTALLED_APPS = (
        ...
        ‘notes’,
        ‘south’,
    )
    ...

## Create your initial migration (Notes: those are two dashes hyphens before initial. The second command uses this initial migration to create your app’s DB tables)
    
    $ python manage.py schemamigration notes --initial
    $ python manage.py migrate notes

# Migrating a changed Model (do the following if you change your data model in models.py later)

1. modify your app’s models.py file    (e.g., add a new column somewhere)

2. run (creates a new migration, note: those are two dashes hyphens before auto):
        
    $ python manage.py schemamigration notes --auto    

3. run (applies this new migration):

    $ python manage.py migrate notes

    That’s it, the very bare bones steps to getting up and running with South. Obviously you’ll either need to run these commands in the same directory as ‘manage.py’ or change the commands to point to it.

# Migration problems (should this be a footnote?)

"Table already exists error" - <http://stackoverflow.com/questions/3090648/django-south-table-already-exists>

Since you already have the tables created in the database, you need to run the initial migration as fake (make sure that the schema of models is same as schema of tables in database.)

    $ python manage.py migrate notes --fake

# Create your views - put in views.py (webnotes/notes/views.py) #

    from django.views.generic.list_detail import object_list
    from django.views.generic.list_detail import object_detail
    from django.views.generic.create_update import create_object
    from django.views.generic.create_update import update_object
    from django.views.generic.create_update import delete_object
    from django.core.urlresolvers import reverse

    from models import Notes

    def notes_list(request):
        """Show all notes"""

        return object_list(request, 
            queryset=Notes.objects.all(),
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

    def notes_create(request):
        """Create new noew"""

        return create_object(request,
            model=Notes,
            template_name='notes/create.html',
            post_save_redirect=reverse("notes_list")
        )            

    def notes_update(request, id):
        """Update note based on id"""

        return update_object(request,
            model=Notes,
            object_id=id,
            template_name='notes/update.html',
            post_save_redirect=reverse("notes_list")
        )            

    def notes_delete(request, id):
        """Delete a note based on id"""

        return delete_object(request,
            model=Notes,
            object_id=id,
            template_name='notes/delete.html',
            post_delete_redirect=reverse("notes_list")
        )

# Create URLs for your notes app - create urls.py inside notes app folder (webnotes/notes/urls.py) - and put the following inside the file and save it #

    from django.conf.urls.defaults import *

    import views

    urlpatterns = patterns('', 

        url(r'^$', views.notes_list, name='notes_list'),  
        url(r'^(?P<id>\d+)/$', views.notes_detail, name='notes_detail'),  
        url(r'^new/$', views.notes_create, name='notes_create'),  
        url(r'^update/(?P<id>\d+)/$', views.notes_update, name='notes_update'),  
        url(r'^delete/(?P<id>\d+)/$', views.notes_delete, name='notes_delete'),  
    )

# Create URLs for your project - include app urls in main urls.conf of our project (webnotes/urls.py)

    from django.conf.urls.defaults import *

    urlpatterns = patterns('',
        (r'^notes/', include('notes.urls')),

# Run development server - and then go to http://127.0.0.1:8000/notes/ #



    $ python manage.py runserver
    
# TODO: 

- Enable admin app and create admin superuser
- Deployment to production server with Nginx/Gunicorn
- PYTHONPATH explanation ?
- virtualenvwrapper ?