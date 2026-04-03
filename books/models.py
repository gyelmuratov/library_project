from django.db import models



class Book(models.Model):
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    content = models.TextField()
    author = models.CharField(max_length=128)
    isbn = models.CharField(max_length=13)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.title
