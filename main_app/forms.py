from django.forms import ModelForm
from .models import Comment
from django.contrib.auth.models import User

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['content']