from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.generate_entry, name="entry"),
    path("wiki", views.entry, name="wiki"),
]
