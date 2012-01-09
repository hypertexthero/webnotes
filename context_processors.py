# http://stackoverflow.com/questions/4256145/django-template-tag-to-display-django-version
import django
def django_version(request):
    return { 'django_version': django.VERSION }