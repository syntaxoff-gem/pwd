from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page_view),
    path("about/", views.about_page_view),
    path("<str:name>/", views.hello_name),
]
