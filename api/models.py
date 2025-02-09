from django.db import models



# Create your models here.


    
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    nationality = models.CharField(max_length=100)
    

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author,related_name='books',on_delete=models.CASCADE)
    publication_date = models.DateField()