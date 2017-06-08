import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page


def populate():

    python_pages = [{"title": "official Python Tutorial", "url": "http://docs.python.prg/2/tutorial"}, {"title": "How to Think like a Computer Scientist","url": "http://www.greenteapress.com/thinkpython/"},
                    {"title": "Learn Python in 10 Minutes", "url": " http://www.korokithakis.net/tutorials/python/"}]

    python_pages_views = 128

    python_pages_likes = 64

    django_pages = [{"title": "Official Django Tutorial", "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
                    {"title": "Django Rocks", "url": "http://www.djangorocks.com/"},
                    {"title": "How to Tango with Django", "url": "http://www.tangowithdjango.com/"}]
    django_pages_views = 64

    django_pages_likes = 32

    other_pages = [{"title": "Bottle","url": "http://bottlepy.org/docs/dev/"},
                   {"title": "Flask","url": "http://flask.pocoo.org"}]
    other_pages_views = 32

    other_pages_likes = 16
    cats = {"Python": {"pages": python_pages, "views": python_pages_views, "likes": python_pages_likes},"Django": {"pages": django_pages, "views": django_pages_views, "likes": django_pages_likes},
             "Other Frameworks": {"pages": other_pages, "views": other_pages_views, "likes": other_pages_likes}}


    for cat, cat_data in cats.items():
            def add_page(cat,title, url, views = 0):
                p = Page.objects.get_or_create(category=cat, title=title)[0]
                p.url = url
                p.views = views
                p.save()
                return p

            def add_cat(name, views, likes):
                c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
                c.save()
                return c

            c = add_cat(cat, cat_data['views'],cat_data['likes'])
            for p in cat_data["pages"]:
                add_page(c, p["title"], p["url"])
            for c in Category.objects.all():
                for p in Page.objects.filter(category=c):
                    print("- {0} - {1}". format(str(c), str(p)))

# Start execution here!
if __name__ == '__main__':
    print(" Starting Rango population script...")
    populate()

