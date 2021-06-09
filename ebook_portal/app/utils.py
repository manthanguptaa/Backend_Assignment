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
    for i in dataObjectList:
        html+= f'''<div class="column is-one-quarter">
        <div class="card mt-6">
            <div class="card-image">
                <figure class="image is-4by3">
                  <img src="{i.cover_book_photo}" alt="Placeholder image">
                </figure>
              </div>
            <div class="card-content">
                <div class="content">
                    <strong>Book Name:</strong> {i.book_name}
                </div>
                <div class="content">
                    <strong>Author:</strong> {i.author.username}
                </div>
                <div class="content">
                    <strong>Published At:</strong> {i.publish_date.date().strftime('%B %d, %Y')}
                </div>
                <footer class="card-footer">
                    <a href="summary/{i.book_slug}" class="card-footer-item">View Book</a>
                </footer>
            </div>
        </div>
    </div>'''  
    html+='</div>' 
    return html


def is_url_image(url):    
    mimetype,encoding = mimetypes.guess_type(url)
    return (mimetype and mimetype.startswith('image'))

def check_url(url):
    """Returns True if the url returns a response code between 200-300,
       otherwise return False.
    """
    try:
        headers = {
            "Range": "bytes=0-10",
            "User-Agent": "MyTestAgent",
            "Accept": "*/*"
        }

        req = urllib3.Request(url, headers=headers)
        response = urllib3.urlopen(req)
        return response.code in range(200, 209)
    except Exception:
        return False

def is_image_and_ready(url):
    return is_url_image(url) and check_url(url)
