import datetime
from django.contrib.admin.options import csrf_protect_m
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import book
from datetime import date, tzinfo
from django.core.paginator import Paginator

# Create your views here.


def getAllBooks(request):
    """
        A function to get all the books from DB and display it on the landing page as a catalogue
    """
    if request.method == 'GET':
        books_result = book.objects.all().order_by("-publish_date")
        # Paginate the results into batches of 10
        paginator = Paginator(books_result,10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        return render(request, "landing_page.html", {"user": User, "current_user_id": request.user.id, 'page_obj': page_obj})


def postBook(request):
    """
        A function to get the user enetered data about the book and create a new row inside DB
    """
    print(request.body)
    if request.method == 'POST':
        if request.user.id:
            book_name = request.POST.get('title')
            language = request.POST.get('lng')
            publish_date = datetime.datetime.now()
            summary = request.POST.get('summary')
            content = request.POST.get('content')
            request.user.book_set.create(book_name=book_name, language=language, publish_date=publish_date, summary=summary, content=content)
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/login")

        

def addBookPage(request):
    """
        Function to render add_book_page.html file
    """
    if request.user.id:
        return render(request, "add_book_page.html")
    else:
        return HttpResponseRedirect("/login")


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
        context = {"books": list(books_byAuthor)}
        return render(request,"search_result_page.html", context)



def myBooks(request):
    """
        A function to get all the books by the current user and display it
    """
    if request.method == 'GET':
        if(request.user.id):
            user_id = request.GET.get('id')
            if user_id:
                book_info = book.objects.filter(author__id__iexact = user_id)
                return render(request, "mybooks_page.html", {"books": list(book_info), "user": User})
            else:
                return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/login")
