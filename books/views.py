from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import Book, IssueBook
from accounts.models import Student
from django.db.models import Q

def home(request):

    search = request.GET.get("search")

    if search:
        books = Book.objects.filter(
            Q(title__icontains=search) |
            Q(author__icontains=search)
        )
    else:
        books = Book.objects.all()

    return render(request, "books.html", {
        "books": books
    })

@login_required
def issue_book(request, id):

    book = get_object_or_404(Book, id=id)

    already_issued = IssueBook.objects.filter(
        user=request.user,
        book=book
    ).exists()

    if not already_issued and book.quantity > 0:

        IssueBook.objects.create(
            user=request.user,
            book=book
        )

        book.quantity -= 1
        book.save()

    return redirect("my_books")


@login_required
def my_books(request):
    issued_books = IssueBook.objects.filter(
        user=request.user
    )

    return render(
        request,
        "my_books.html",
        {
            "issued_books": issued_books
        }
    )


@login_required
def return_book(request, id):

    issued_book = get_object_or_404(
        IssueBook,
        id=id,
        user=request.user
    )

    book = issued_book.book

    book.quantity += 1
    book.save()

    issued_book.delete()

    return redirect("my_books")


@login_required
def dashboard(request):

    books = Book.objects.all()

    total_books = Book.objects.count()

    available_books = Book.objects.filter(quantity__gt=0).count()

    issued_books = IssueBook.objects.count()

    total_students = Student.objects.count()

    return render(
        request,
        "dashboard.html",
        {
            "books": books,
            "is_admin": request.user.is_staff,
            "total_books": total_books,
            "available_books": available_books,
            "issued_books": issued_books,
            "total_students": total_students,
        }
    )
@login_required
def profile(request):

    if request.user.is_staff:
        return render(request, "profile.html", {
            "admin": True
        })

    student = Student.objects.filter(user=request.user).first()

    return render(request, "profile.html", {
        "student": student,
        "admin": False
    })
