from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import requests 
import json
from itertools import chain
from .forms import CommentForm
from . models import Word, Comment

@login_required
def words(request):
  #retrieve two words from api
  r = requests.get("https://random-word-api.herokuapp.com/word?number=2").json()

  #isolate each word
  word_one = r[0]
  word_two = r[1]

  #save word pair to the database
  new_word = Word.objects.create(word_one = word_one, word_two = word_two, user_id = request.user.id)

  context = {
    'new_word' : new_word,
  }
  return render (request, 'twowords/index.html', context)


@login_required
def words_list(request):

  #query for words that have been commented on by the user and order them by most recently created
  user_words = Word.objects.filter(user=request.user)
  words = user_words.exclude(comment__content = None).order_by('-id')

  context = {
    'words' : words,
  }
  return render(request, 'twowords/list.html', context)


def about(request):
  return render(request, 'about.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


@login_required
def words_detail(request, word_id):
  word = Word.objects.get(id=word_id)
  comments = Comment.objects.filter(word=word).order_by('-id')
  comment_form = CommentForm()
  context = {
    'word': word,
    'comments' : comments,
    'comment_form' : comment_form
  }
  return render(request, 'twowords/detail.html', context)


@login_required
def add_comment(request, word_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.word_id = word_id
    new_comment.save()
  return redirect('detail', word_id=word_id)

