from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Word(models.Model):
    word_one = models.CharField(max_length=25)
    word_two = models.CharField(max_length=25)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __init__(self, word_one, word_two):
    #     self.word_one = word_one


    # def from_json(cls, json_string):
    #     json_dict = json.loads(json_string)
    #     return cls(**json_dict)

    # def __repr__(self):
    #     self.word_one
    #     self.word_two

    def __str__(self):
        return '{} {} {}'.format(self.word_one, self.word_two, self.user)