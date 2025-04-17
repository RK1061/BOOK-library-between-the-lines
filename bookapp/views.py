from django.shortcuts import render, redirect
from bookapp.models import Book

# Create your views here.
def index(request):
    books = Book.objects.all()
    print(type(books))
    print(books)
    context={}
    context['books']=books
    return render (request, "index.html",context)

def addbook(request):
    print('Method :',request.method)

    if request.method== "GET":
        return render(request,'addbook.html')
    else:
        t = request.POST["title"].lower()
        a = request.POST["author"].lower()
        p = request.POST["price"]
        book = Book.objects.create(title= t, author=a, price=p)
        book.save()
        # return render (request, "index.html" )
        return redirect('/')
    
def deleteBook(request, bookid):
    book = Book.objects.filter(id=bookid)
    book.delete()
    return redirect("/")

def editBook(request, bookid):
    if request.method == "GET":
        book = Book.objects.get(id=bookid)
        context = {"book" : book}
        return render(request, "editbook.html", context)
    else:

        t = request.POST["title"].lower()
        a = request.POST["author"].lower()
        p = request.POST["price"]
        book = Book.objects.filter(id=bookid)
        book.update(title=t, author=a, price=p)

        return redirect('/')
