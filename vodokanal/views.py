from django.shortcuts import render, get_object_or_404
from .models import Job
from .models import Photo
from .models import News

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job.html', {'jobs': jobs})
def photo_gallery(request):
    photos = Photo.objects.all()
    return render(request, 'gallery.html', {'photos': photos})
def news_list(request):
    news_list = News.objects.all()
    return render(request, 'news.html', {'news_list': news_list})
def news_detail(request, pk):
    single_news = get_object_or_404(News, pk=pk)
    return render(request, 'article.html', {'single_news': single_news})
def main_page(request):
    return render(request, 'index.html')
def contacts_page(request):
    return render(request, 'contacts.html')
