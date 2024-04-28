from django.db import models

# Create your models here.


class Assigment(models.Model):
    name = models.CharField(max_length=123)
    describtion = models.TextField()
    file = models.FileField(upload_to='files')

    def __str__(self):
        return self.name