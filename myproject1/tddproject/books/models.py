# Create your models here.
import datetime
from django.utils import timezone
from django.db import models


# ... #

class Author(models.Model):
    authorname = models.CharField(max_length=20)
    authortel = models.CharField(max_length=50)

    def __str__(self):
        return self.authorname


class Publisher(models.Model):
    publishername = models.CharField(max_length=20)
    publishertel = models.CharField(max_length=50)

    def __str__(self):
        return self.publishername


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    # publisher = models.ForeignKey(Publisher)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    publication_date = models.DateField()

    # def __init__(self, publication_date):
    #     self.publication_date =  publication_date

    def recent_publication(self):
        # 일반 연산자는 >= 보다 - 가 우선순위 높음
        # 최근 8주내에 출간한 책인지 판단
        return self.publication_date >= timezone.now().date() - datetime.timedelta(weeks=8)

    # ... #
