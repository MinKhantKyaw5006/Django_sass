from django.http import HttpResponse
# django way
from django.shortcuts import render
# python way
import pathlib

this_dir = pathlib.Path(__file__).resolve().parent


def home_page_view(request, *args, **kwargs):
    my_title = "My Page"
    my_context = {
        "page_title": my_title
    }
    html_template = "home.html"
    return render(request, html_template, my_context)


def my_old_home_page_view(request, *args, **kwargs):
    my_title = "My Page"
    my_context = {
        "page_title": my_title
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
