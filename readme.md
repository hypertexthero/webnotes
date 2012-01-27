I started with [this excellent tutorial](http://komunitasweb.com/2010/02/django-tutorial-simple-notes-application/). The code is liberally commented.

—[Simon Griffee](http://hypertexthero.com)

Features
========

- [Markdown (including footnotes support) for editing, HTML for display](https://code.djangoproject.com/wiki/UsingMarkup) with live preview courtesy of [WMD](https://github.com/ChiperSoft/wmd#readme).
- Dates on homepage are displayed only once for notes published on the same day. Using '[ifchanged](https://docs.djangoproject.com/en/dev/ref/templates/builtins/?from=olddocs#ifchanged).'
- Code syntax highlighting in markup courtesy of [Pygments](http://pygments.org/) and [CodeHilite](http://freewisdom.org/projects/python-markdown/CodeHilite).
- Clean, logical URLs (in progress).
- Simple interface (in progress).

To Do
=====

- Customize published date field with [lightweight](http://stefangabos.ro/jquery/zebra-datepicker/) datepicker widget?
- Implement [django static generator](https://github.com/luckythetourist/staticgenerator) so we are *serving static files in HTML on server*. Also try to find a way to have static files in Markdown format on the server.
- [Fixtures](https://docs.djangoproject.com/en/dev/ref/django-admin/#what-s-a-fixture) example for a note demonstrating Markdown with footnotes, syntax highlighting and nice typography courtesy of [typogryfy](http://code.google.com/p/typogrify/).
- One-click download of all notes in `.txt` (plain text in Markdown format) or `.html` format for easy backup.
- [Messages](https://docs.djangoproject.com/en/dev/ref/contrib/messages/) for display after adding, updating and deleting notes, maybe using [Ajax](http://webcloud.se/log/AJAX-in-Django-with-jQuery/).
- Change permalink of notes to slug instead of id(?)
- Create date-based archive pages, with clickable dates on front page list.
- Use jQuery [timeago plugin](http://timeago.yarp.com/) for dates?
- Two categories for notes: links (to other content) and articles (original articles).
- XML/RPC API for remote publishing.
- Atom/RSS feeds.
- Auto-save on note editing views?