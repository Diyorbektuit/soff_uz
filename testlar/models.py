from django.db import models
from category.models import Category
from django.contrib.auth.models import User
# Create your models here.


class Test(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    testlar_soni = models.IntegerField()
    height_score = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    number = models.PositiveIntegerField()
    question = models.TextField()
    a = models.TextField()
    b = models.TextField()
    c = models.TextField()
    d = models.TextField()
    true_answer = models.CharField(max_length=150, help_text='E.x = a')

    def __str__(self):
        return self.question


