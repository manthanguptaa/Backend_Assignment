from django.contrib.admin.options import csrf_protect_m
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import book
from datetime import date
from django.core.paginator import Paginator

# Create your views here.


def getAllBooks(request):
    """
        A function to get all the books from DB and display it on the landing page as a catalogue
    """
    if request.method == 'GET':
        books_result = book.objects.all().order_by("-publish_date")
        # Paginate the results into batches of 25
        paginator = Paginator(books_result,25)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        return render(request, "landing_page.html", {"user": User, "current_user_id": request.user.id, 'page_obj': page_obj})


def postBook(request):
    """
        A function to get the user enetered data about the book and create a new row inside DB
    """
    if request.method == 'POST':
        book_name = request.POST.get('title')
        language = request.POST.get('lng')
        published_date = date.today()
        summary = request.POST.get('summary')
        content = request.POST.get('content')
        # TODO DJango login required decorator
        print(book_name, language, published_date, summary, content)
        request.user.book_set.create(book_name=book_name, language=language, published_date=published_date, summary=summary, content=content)
        

def addBookPage(request):
    postBook(request)
    return render(request, "add_book_page.html")


def bookInfo(request):
    """
        A function to get all the info related to a book by it's book_id
    """
    if request.method == 'GET':
        book_id = request.GET.get('id')
        book_info = book.objects.filter(id__exact=book_id)
        
        return book_info


def summaryPage(request):
    """
        Function for rendering summary page
    """
    book_info = bookInfo(request)
    return render(request, "summary_page.html", {"books":list(book_info)})


def readStoryPage(request):
    """
        Function for rendering the read full story page
    """
    book_info = bookInfo(request)
    return render(request, "read_full_story_page.html",{"books":list(book_info)})



def searchForBook(request):
    """
        A function to get all the books that match the search query
    """
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        print(search_query)
        books_byAuthor = book.objects.filter(author__username__icontains=search_query)
        books_byName = book.objects.filter(book_name__iexact=search_query)
        print(books_byName,books_byAuthor)
        # helper(request,books)

def helper(request, books):
    if request.method == 'GET':
        return render(request,"search_result_page.html",{"books": list(books)})


def myBooks(request):
    """
        A function to get all the books by the current user and display it
    """
    if request.method == 'GET':
        user_id = request.GET.get('id')
        book_info = book.objects.filter(author__id__iexact = user_id)
        
        return render(request, "mybooks_page.html", {"books": list(book_info)})
