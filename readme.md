I started with [this excellent tutorial](http://komunitasweb.com/2010/02/django-tutorial-simple-notes-application/). The code is liberally commented.

—[Simon Griffee](http://hypertexthero.com)

Features
========

- [Markdown for editing, HTML for display](https://code.djangoproject.com/wiki/UsingMarkup).
- Dates on homepage are displayed only once for notes published on the same day. Using '[ifchanged](https://docs.djangoproject.com/en/dev/ref/templates/builtins/?from=olddocs#ifchanged) '.
- Clean, logical URLs (in progress).
- Simple interface (in progress).

To Do
=====

- <del>Find out how to increase size of form inputs in template files rather than using modelforms/'widgets' in models.py</del>.
    - Customize created and modified fields with existing django datepicker widget.
- Implement [django static generator](https://github.com/luckythetourist/staticgenerator) so we are *serving static files in HTML on server*. Also try to find a way to have static files in Markdown format on the server.
- Create a [fixtures](https://docs.djangoproject.com/en/dev/ref/django-admin/#what-s-a-fixture) example for a post demonstrating Markdown with footnotes, syntax highlighting and nice typography courtesy of [typogryfy](http://code.google.com/p/typogrify/).
- One-click download of all notes in .txt (Markdown) or .html format for easy backup.
- Markdown editing preview with [WMD](https://github.com/ChiperSoft/wmd#readme).
- [Messages](https://docs.djangoproject.com/en/dev/ref/contrib/messages/) for display after adding, updating and deleting notes, maybe using [Ajax](http://webcloud.se/log/AJAX-in-Django-with-jQuery/).
- Change permalink of notes to slug instead of id(?)
- Use jQuery [timeago plugin](http://timeago.yarp.com/) for dates?
- Two categories for notes: links (to other content) and articles (original articles).
- XML/RPC API for remote publishing.
- Atom/RSS feeds
