from django.http import HttpResponse
# python way
import pathlib

this_dir = pathlib.Path(__file__).resolve().parent


def home_page_view(request, *args, **kwargs):
    html = ""
    html_file_path = this_dir / "home.html"
    html = html_file_path.read_text()
    return HttpResponse(html)
