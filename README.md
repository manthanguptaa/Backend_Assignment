# Backend Assignment
> E-Book Platform where users can sign up & view/read/add a list of books available.

## Tech-Stack Used
1. Django
2. DB: sqlite3 (inbuilt)

## DB Schema
![Untitled (2)](https://user-images.githubusercontent.com/42516515/121385594-e02fac80-c966-11eb-9522-b42982811480.png)

## Setup
1. `git clone https://github.com/Manthan109/Backend_Assignment.git`
2. `cd Backend_Assignment/`
3. `pip install virtualenv`
4. `python3 -m venv pratilipi`
5. `source pratilipi/bin/activate`
6. `pip install -r requirements.txt`
7. `cd ebook_portal/`
8. `gunicorn ebook_portal.wsgi`

## Assumptions & Reasoning

<p>I have added slug for uniquely identifying an individual book. The reason to use slug was to not return the internal id used within the database
and preserving the ability to see, at a glance, what the item is. This makes the search engine optimized URLs.</p>

<p>I have limited the content and summary to 3000 and 500 chars respectively which is not the best way to do it but have implemented it for simplicity.</p>

<p>I have allowed anonymous users to be able to browse through the website and read the story but restricted them from posting a book and looking at the My Books tab. This came by taking inspiration from Pratilipi's website and from some e-commerce websites which makes sense.</p>