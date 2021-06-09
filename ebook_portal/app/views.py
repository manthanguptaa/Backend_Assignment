import datetime
from ebook_portal.settings import DEFAULT_COVER_IMAGE_URL
from .utils import bookInfo, helper, CustomError, is_image_and_ready
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import book
from datetime import date, tzinfo
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def getAllBooks(request):
    """
        A function to get all the books from DB and display it on the landing page as a catalogue
    """
    books_result = book.objects.all().order_by("-publish_date")
    # Paginated the results into batches of 10
    paginator = Paginator(books_result,12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
        
    return render(request, "landing_page.html", {"current_user_id": request.user.id, 'page_obj': page_obj})


@login_required(login_url='/login')
def postBook(request):
    """
        A function to get the user enetered data about the book and create a new row inside DB
    """
    book_name = request.POST.get('title')
    language = request.POST.get('lng')
    publish_date = datetime.datetime.now()
    summary = request.POST.get('summary')
    content = request.POST.get('content')
    cover_image = request.POST.get('cover_image')
    if not is_image_and_ready(cover_image):
        cover_image = DEFAULT_COVER_IMAGE_URL
    try:
        request.user.book_set.create(book_name=book_name, language=language, publish_date=publish_date, summary=summary, content=content, cover_book_photo=cover_image)
    except Exception as e:
        raise CustomError("Something is wrong!")
    return HttpResponseRedirect("/")

 
@login_required(login_url="/login")
def addBookPage(request):
    """
        Function to render add_book_page.html file
    """
    return render(request, "add_book_page.html")


def summaryPage(request, slug):
    """
        Function for rendering summary page
    """
    slug = slug.split('-')[-1]
    book_info = bookInfo(slug)
    return render(request, "summary_page.html", {"books":book_info})


def readStoryPage(request, slug):
    """
        Function for rendering the read full story page
    """
    slug = slug.split('-')[-1]
    book_info = bookInfo(slug)
    return render(request, "read_full_story_page.html",{"books":book_info})


def searchForBook(request):
    """
        A function to get all the books that match the search query
    """

    search_query = request.POST.get('search_query')
    books_by_author = book.objects.filter(author__username__icontains=search_query)
    books_by_name = book.objects.filter(book_name__iexact=search_query)
    return JsonResponse({"data": helper(list(books_by_author | books_by_name))})


@login_required(login_url="/login")
def myBooks(request):
    """
        A function to get all the books by the current user and display it
    """
    user_id = request.user.id
    book_info = book.objects.filter(author__id__iexact = user_id)
    return render(request, "mybooks_page.html", {"books": list(book_info)})
