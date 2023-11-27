from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=30)
    birth_date = models.DateField()
    biography = models.TextField(max_length=1000)

    def str(self):
        return self.name




class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    publication_data = models.DateField(default=timezone.now)
    price = models.IntegerField()


    def str(self):
        return self.title




class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=30)
    content = models.TextField(max_length=500)


    def str(self):
        return self.reviewer_name

   

   