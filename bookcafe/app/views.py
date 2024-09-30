from django.shortcuts import render,get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Book
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    book=Book.objects.all()
    query=request.GET.get("query","").strip()
    if query:
        book_list = book.filter(title__icontains=query)
    else:
        book_list=book
    return render(request,"app/home.html",
                  {
                      'bookinfo':book_list,
                      'query':query,
                  })
@login_required
def id(request:HttpRequest,pk:int)-> HttpResponse:
    book=get_object_or_404(Book,pk=pk)
    return render(request,"app/id.html",
                  {
                      'bookkk':book,
                  })
    