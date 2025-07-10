from visits.models import PageVisit
from django.http import HttpResponse
# django way
from django.shortcuts import render
# python way
import pathlib


this_dir = pathlib.Path(__file__).resolve().parent

# import the model


def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "page_visit_count": page_qs.count(),
        "percent": (page_qs.count() * 100.0) / qs.count(),
        "total_visit_count": qs.count(),
    }
    # path = request.path
    # print("path", path)
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)


def my_old_home_page_view(request, *args, **kwargs):
    my_title = "My Page"
    my_context = {
        "page_title": my_title,

    }
    html_ = """
        <!DOCTYPE html>
        <html>
            <body>
                <h1>{page_title}</h1>
            </body>
        </html>
""".format(**my_context)  # page_title = my_title
    html_file_path = this_dir / "home.html"
    html = html_file_path.read_text()
    return HttpResponse(html)
