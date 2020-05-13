from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Word(models.Model):
    word_one = models.CharField(max_length=25)
    word_two = models.CharField(max_length=25)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.word_one, self.word_two

