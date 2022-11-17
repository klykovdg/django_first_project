from django.contrib import admin
from django.urls import path
from mysite.views import hello, display_meta
from mysite.views import get_date
from mysite.views import hours_ahead
from books import views


urlpatterns = [
    path('admin/', admin.site.urls), path('hello/', hello), path('time/', get_date),
    path('time/plus/<int:hour>/', hours_ahead), path('meta/', display_meta),
    path('search-form/', views.search_form), path('search/', views.search),
    path('contact/', views.contact), path('contact/thanks/', views.thanks),
]
