from django.contrib import admin
from .models import Job
from .models import Photo
from .models import News
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'requirement1', 'requirement2', 'requirement3', 'salary', 'contact',
]
@admin.register(Photo)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image',
]
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'image', 'article',
]
