from django.shortcuts import render
from django.http import HttpResponse


def hello_name(request, name: str):
    context = {"name": name.title()}
    return render(request, "pages/by_name.html", context)


def home_page_view(request):
    return HttpResponse("Homepage".encode("utf-8"))


def about_page_view(request):
    return render(request, "pages/about.html", context={"name": "Sofia", "age": 21})
