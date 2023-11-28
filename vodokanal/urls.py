from django.urls import path
from . import views
from .views import job_list, photo_gallery, news_list

urlpatterns = [
    path('job/', job_list, name='job_list'),
    path('gallery/', photo_gallery, name='photo_gallery'),
    path('news/', news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
    path('', views.main_page, name='main_page'),
    path('contacts/', views.contacts_page, name='contacts_page'),
]