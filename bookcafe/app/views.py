from django.shortcuts import render,get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Book
# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    book=Book.objects.all()
    return render(request,"app/home.html",
                  {
                      'bookinfo':book,
                  })
def id(request:HttpRequest,pk:int)-> HttpResponse:
    book=Book.objects.all()
    return render(request,"app/id.html",
                  {
                      'bookkk':book,
                  })