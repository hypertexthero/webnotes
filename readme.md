The code is liberally commented.

—[Simon Griffee](http://hypertexthero.com)

To Do
=====

- <del>Find out how to increase size of form inputs in template files rather than using modelforms/'widgets' in models.py</del>
    - Customize created and modified fields with existing django datepicker widget.
- Combine [django static generator](https://github.com/luckythetourist/staticgenerator) with the [Markdown for editing, HTML for displaying functionality](https://code.djangoproject.com/wiki/UsingMarkup) so we are *serving static files in HTML on server* and Markdown and HTML columns in database. Also try to find a way to have static files in Markdown format on the server.
- Create [fixtures](https://docs.djangoproject.com/en/dev/ref/django-admin/#what-s-a-fixture) for a post demonstrating Markdown with footnotes and syntax highlighting.
- Implement one-click download of all notes in .txt (Markdown) or .html format for easy backup.
- Implement Markdown editing preview with [WMD](https://github.com/ChiperSoft/wmd#readme).
- Implement [messages](https://docs.djangoproject.com/en/dev/ref/contrib/messages/) for display after adding, updating and deleting notes, maybe using [Ajax](http://webcloud.se/log/AJAX-in-Django-with-jQuery/).
- Change permalink of notes to slug instead of id?
- Add published date under article title in detail page and modified date in footer of detail page. Maybe use jQuery [timeago plugin](http://timeago.yarp.com/).
- <del>Date line on homepage. Changes only when published date of articles change. Use '[ifchanged](https://docs.djangoproject.com/en/dev/ref/templates/builtins/?from=olddocs#ifchanged.)'</del>
- Implement two categories for notes: links (to other content) and articles (original articles)
- Implement XML/RPC remote publishing
