from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from books.models import *
from django.template import Context

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            authors = Author.objects.filter(name=q)
            if len(list(authors)) == 0:
                return HttpResponse("no author")
#            books = Book.objects.filter(authorid=author.authorid)
            for a in authors:
                books = a.book_set.all()
                print books
#            books = Book.objects.get(title=q)
                return render(request, 'search_results.html', {'books': books, 'query': q})
    return render(request, 'search_form.html', {'error': error})
        
def addbook(request):
    if request.POST:
        post = request.POST
        newbook = Book(
            isbn = post["isbn"],
            title = post["title"],
            author = Author.objects.get(authorid=post["authorid"]),
            authorid = post["authorid"],
            publisher = post["publisher"],
            publishdate = post["publishdate"],
            price = post["price"])
        newbook.save()
#        try:
#            Author.objects.get(authorid = post["authorid"])
#        except:
#            addauthor(request)
    return render(request, "addbook_form.html", {'authorlist': Author.objects.all},)
    
def addauthor(request):
    if request.POST:
        post = request.POST
        newauthor = Author(
            authorid = post["authorid"],
            name = post["name"],
            age = post["age"],
            country = post["country"])
        newauthor.save()
    return render(request, "addauthor_form.html")
        
def booklist(request):
    try:
        deletebook = Book.objects.get(id = request.GET["id"])
        deletebook.delete()
        booklist = Book.objects.all()
        c = Context({"booklist": booklist,})
        return render(request, "book_list.html", c)
    except:
        booklist = Book.objects.all()
        c = Context({"booklist": booklist,})
        return render(request, "book_list.html", c)
    
def authorlist(request):
    try:
        deleteauthor = Author.objects.get(id = request.GET["id"])
        deleteauthor.delete()
        authorlist = Author.objects.all()
        c = Context({"authorlist": authorlist,})
        return render(request, "author_list.html", c)
    except:
        authorlist = Author.objects.all()
        c = Context({"authorlist": authorlist,})
        return render(request, "author_list.html", c)

def information(request):
#    bookid = request.GET['id']
#    thebook = Book.objects.get(id='book.id')
#    return render_to_response('information.html', {'thebook': thebook}, {'title': thebook.title})
    book = Book.objects.get(id = request.GET["id"])
    
    
    author = Author.objects.get(authorid = book.authorid)
    
    c = Context({"book":book, "author": author,})
    return render(request, "information.html", c)
        
def updatebook(request):
    updatebook = Book.objects.get(id=request.GET["id"])
    updatebook.delete()
    if request.POST:
        post = request.POST
        newbook = Book(
            isbn = post["isbn"],
            title = post["title"],
            authorid = post["authorid"],
            author = Author.objects.get(authorid=post["authorid"]),
            publisher = post["publisher"],
            publishdate = post["publishdate"],
            price = post["price"])
        newbook.save()
    booklist = Book.objects.all()
    c = Context({"booklist": booklist,})
    return render(request, "book_list.html", c)

def updatebookform(request):
    updatebook = Book.objects.get(id=request.GET["id"])
    c = Context({'updatebook': updatebook,})
    return render(request, "updatebookform.html", c)

def index(request):
    return render(request, "index.html")
