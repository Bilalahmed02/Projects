"""
A relational database is structured, meaning the data is organized in tables. Many times, 
the data within these tables have relationships with one another, or dependencies.A non 
relational database is document-oriented, meaning, all information gets stored in more of 
a laundry list order.

"""

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 50)
    description =models.TextField(max_length = 1000)
    author = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title


class Review(models.Model):
    rating = models.FloatField()
    comment = models.TextField(max_length = 500)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.article.author


