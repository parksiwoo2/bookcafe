from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Book
# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    book=Book.objects.all()
    return render(request,"app/home.html",
                  {
                      'bookinfo':book,
                  })