from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),

    path(
        "issue/<int:id>/",
        views.issue_book,
        name="issue_book"
    ),

    path(
        "my-books/",
        views.my_books,
        name="my_books"
    ),
    path(
    "return/<int:id>/",
    views.return_book,
    name="return_book"
    ),
    path(
    "dashboard/",
    views.dashboard,
    name="dashboard"
    ),
     path("profile/", views.profile, name="profile"),
]