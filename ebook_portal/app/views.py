from django.contrib.admin.options import csrf_protect_m
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import book
from datetime import date

# Create your views here.


def getAllBooks(request):
    """
        A function to get all the books from DB and display it on the landing page as a catalogue
    """
    if request.method == 'GET':
        books = book.objects.all().order_by("-publish_date")
        # book_dict = dict(books)
        # print(book_dict)
        # TODO paginate the results
        print(request.user.id)
        return render(request, "landing_page.html", {"books":list(books), "user": User, "current_user_id": request.user.id})


def postBook(request):
    """
        A function to get the user enetered data about the book and create a new row inside DB
    """
    if request.method == 'POST':
        book_name = request.GET.get('title')
        language = request.GET.get('lng')
        published_date = date.today()
        summary = request.GET.get('summary')
        content = request.GET.get('content')
        # TODO DJango login required decorator
        request.user.book_set.create(book_name=book_name, language=language, published_date=published_date, summary=summary, content=content)
        

def addBookPage(request):
    return render(request, "add_book_page.html")


def bookInfo(request):
    """
        A function to get all the info related to a book by it's book_id
    """
    if request.method == 'GET':
        book_id = request.GET.get('id')
        book_info = book.objects.filter(id__exact=book_id)
        print(book_info)
        return book_info


def summaryPage(request):
    book_info = bookInfo(request)
    return render(request, "summary_page.html", {"books":list(book_info)})


def readStoryPage(request):
    book_info = bookInfo(request)
    return render(request, "read_full_story_page.html",{"books":list(book_info)})



def searchForBook(request):
    """
        A function to get all the books that match the search query
    """
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        print(search_query)
        # TODO add for 
        books = book.objects.filter(author__username__icontains=search_query)
        print(books.query)
        return render(request,"search_result_page.html",{"books": list(books)})


def myBooks(request):
    """
        A function to get all the books by the current user and display it
    """
    if request.method == 'GET':
        user_id = request.GET.get('id')
        book_info = book.objects.filter(author__id__iexact = user_id)
        print(book_info)
        return render(request, "mybooks_page.html", {"books": list(book_info)})