"""ebook_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.views.static import serve
from user_authentication import views as v
from app import views as l


urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", v.register, name="register"),
    path("", include("django.contrib.auth.urls")),
    path("", l.getAllBooks, name="home"),
    path("summary/<str:slug>",l.summaryPage, name="summary_page"),
    path("summary/content/<str:slug>", l.readStoryPage, name="full_content_page"),
    path("mybooks/", l.myBooks, name = "my_books"),
    path("mybooks/addbook/", l.addBookPage, name="add_book"),
    path("mybooks/addbook/postbook/", l.postBook),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
