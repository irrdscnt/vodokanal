from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    requirement1 = models.CharField(max_length=255)
    requirement2 = models.CharField(max_length=255)
    requirement3 = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)

    def __str__(self):
        return self.title
class Photo(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    image = models.ImageField(upload_to='news/')
    article = models.TextField()

    def __str__(self):
        return self.title
