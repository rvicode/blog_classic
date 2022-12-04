from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)

    datetime_crated = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=200)
    category = models.ManyToManyField(Category, related_name='category', null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='Article/photo')
    status = models.BooleanField(default=False)

    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

