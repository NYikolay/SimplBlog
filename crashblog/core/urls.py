from django.urls import path
from .views import *

urlpatterns = [
    path('search/', search, name='search'),
    path('', frontpage, name='frontpage'),
    path('about/', about, name='about'),
    path('<slug:category_slug>/<slug:slug>/', detail, name='detail'),
    path('<slug:slug>/', category, name='category'),
]