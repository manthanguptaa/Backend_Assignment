from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import book
from datetime import date
from django.core import serializers

# Create your views here.


def getAllBooks(response):
    """
        A function to get all the books from DB and display it on the landing page as a catalogue
    """
    if response.method == 'GET':
        books = book.objects.all().order_by("-publish_date")
        # book_dict = dict(books)
        # print(book_dict)
        # TODO paginate the results
        return render(response, "landing_page.html", {"books":list(books), "user": User})


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
        request.user.book_set.create(book_name=book_name, language=language, published_date=published_date, summary=summary, content=content)
        return JsonResponse({"result":"success"})


def bookInfo(response):
    """
        A function to get all the info related to a book by it's book_id
    """
    if response.method == 'GET':
        book_id = response.GET.get('id')
        book_info = book.objects.filter(id__exact=book_id)
        print(book_info)
        return book_info


def summaryPage(response):
    book_info = bookInfo(response)
    return render(response, "summary_page.html", {"books":list(book_info)})


def readStoryPage(response):
    book_info = bookInfo(response)
    return render(response, "read_full_story_page.html",{"books":list(book_info)})


def searchForBook(request):
    """
        A function to get all the books that match the search query
    """
    if request.method == 'GET':
        search_query = request.GET.get('query')
        try:
            books = book.objects.filter(author__name__icontains=search_query,book_name__icontains=search_query)
            print(books)
            return JsonResponse({"result":books})
        except Exception as e:
            print(e)
            pass