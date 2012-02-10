I started with [this excellent tutorial](http://komunitasweb.com/2010/02/django-tutorial-simple-notes-application/). The code is liberally commented.

—[Simon Griffee](http://hypertexthero.com)

Features
----

- [Markdown (including footnotes support) for editing, HTML for display](https://code.djangoproject.com/wiki/UsingMarkup) with live preview courtesy of [WMD](https://github.com/ChiperSoft/wmd#readme).
- Dates on homepage are displayed only once for notes published on the same day. Using '[ifchanged](https://docs.djangoproject.com/en/dev/ref/templates/builtins/?from=olddocs#ifchanged).'
- Links and original article note types published to the same content column.
- Code syntax highlighting in markup courtesy of [Pygments](http://pygments.org/) and [CodeHilite](http://freewisdom.org/projects/python-markdown/CodeHilite).
- Simple search
- Simple interface (in progress).

To Do
----

- **Implement clean date-based permalink URLs with filename.html: `Webnotes > 2012 > January > 30 > NoteTile.html`**

    **Article Archive:** `webnotes/archive/` - displays all original articles.
    **Link Archive:** `webnotes/links/` - displays latest 15 links and then a list of past year, month archives in the following format:

    - January 2012
    - December 2011
    - November 2011

    **Link Month Archive:** `webnotes/links/2012/january/` - displays all links for January 2012.
    
- Add get_absolute_url method to Notes model
- Customize published date field with [lightweight](http://stefangabos.ro/jquery/zebra-datepicker/) datepicker widget?
- Modify Markdown footnotes extension (or rather move it into the project) to add datestamp to footnote anchor so footnote links are unique on notes list page displaying more than one article with a footnote. i.e. #fnr1-2012-01-29 instead of #fn:1'- Looks like this is [fixed](http://www.freewisdom.org/projects/python-markdown/Tickets/000037) by setting the unique ids option to True in the python-markdown footnotes extention. May still want to modify it so that the date and time in the format yyyymmdd-hhmmss is the unique_prefix instead of a number.
- Implement [django static generator](https://github.com/luckythetourist/staticgenerator) so we are *serving static files in HTML on server*. Also try to find a way to have static files in Markdown format on the server.
- [Fixtures](https://docs.djangoproject.com/en/dev/ref/django-admin/#what-s-a-fixture) example for a note demonstrating Markdown with footnotes, syntax highlighting and nice typography courtesy of [typogryfy](http://code.google.com/p/typogrify/).
- One-click download of all notes in `.txt` (plain text in Markdown format) or `.html` format for easy backup.
- [Messages](https://docs.djangoproject.com/en/dev/ref/contrib/messages/) for display after adding, updating and deleting notes, maybe using [Ajax](http://webcloud.se/log/AJAX-in-Django-with-jQuery/).
- Use jQuery [timeago plugin](http://timeago.yarp.com/) for dates?
- XML/RPC API for remote publishing.
- Atom/RSS feeds.
- Auto-save on note editing views?

[^1]: /notes-env/lib/python2.6/site-packages/markdown/extensions/footnotes.py

<!-- - Add user profile pages and link user names in the article bylines there. -->