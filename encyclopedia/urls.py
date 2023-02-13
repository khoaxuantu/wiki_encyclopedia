from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.generate_entry, name="entry"),
    path("search", views.entry, name="search"),
    path("createpage", views.create_page, name="create page"),
    path("editpage/<str:entry>", views.edit_page, name="edit page"),
    path("randompage", views.random_page, name="random page")
]
