#Move to utils.py
from .models import book
import mimetypes, urllib3
from django.shortcuts import get_object_or_404

class CustomError(Exception):
    pass


def bookInfo(slug):
    """
        A function to get all the info related to a book by it's book_id
    """
    book_info = get_object_or_404(book, slug=slug)
    return book_info


def helper(dataObjectList):
    """
        A function to process the data and returning html to display cards
    """
    html='<div class="columns is-multiline">'
    for book in dataObjectList:
        html+= f'''<div class="column is-one-quarter">
        <div class="card mt-6">
            <div class="card-image">
                <figure class="image is-4by3">
                  <img src="{book.cover_book_photo}" alt="Placeholder image">
                </figure>
              </div>
            <div class="card-content">
                <div class="content">
                    <strong>Book Name:</strong> {book.book_name}
                </div>
                <div class="content">
                    <strong>Author:</strong> {book.author.username}
                </div>
                <div class="content">
                    <strong>Published At:</strong> {book.publish_date.date().strftime('%B %d, %Y')}
                </div>
                <footer class="card-footer">
                    <a href="summary/{book.book_slug}" class="card-footer-item">View Book</a>
                </footer>
            </div>
        </div>
    </div>'''  
    html+='</div>' 
    return html


def is_url_image(url): 
    """
        Function to check if the url entered is of an image
    """   
    mimetype,encoding = mimetypes.guess_type(url)
    return (mimetype and mimetype.startswith('image'))
