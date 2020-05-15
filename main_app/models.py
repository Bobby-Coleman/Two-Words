from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Word(models.Model):
    word_one = models.CharField(max_length=25)
    word_two = models.CharField(max_length=25)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {}'.format(self.word_one, self.word_two, str(self.user.username))

    
    def get_absolute_url(self):
        return reverse('index', kwargs={'word_id': self.id})

class Comment(models.Model):
    content = models.TextField(max_length=260)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):      
        return f"{self.content} on {self.timestamp}"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'comment_id': self.id})
