from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import requests 
import json
from .forms import CommentForm
# from random_word import RandomWords
from . models import Word, Comment

@login_required
def words(request):
  r = requests.get("https://random-word-api.herokuapp.com/word?number=2").json()
  # print(r)
  # print(type(r))
  # print(x)

  word_one = json.dumps(r[0])
  word_two = json.dumps(r[1])
  # print(request.method)
  # try:
  #   words = json.loads(r.content)

  # except Exception as e:
  #   words = "Error data not loading"

  # words = {
  #     'word_one' : word_one,
  #     'word_two' : word_two,
  # }

  # print(request.user)
  new_word = Word.objects.create(word_one = word_one, word_two = word_two, user_id = request.user.id)
  # print(new_word)
  # comment_form = CommentForm()
  context = {
    'new_word' : new_word,
  }
  return render (request, 'twowords/index.html', context)


@login_required
def words_list(request):
  #change to words that are saved by user
  words = Word.objects.filter(user=request.user)

  # words = Word.objects.all()

  context = {
    'words' : words,
  #  'comments' : comments,
  }
  return render(request, 'twowords/list.html', context)

# { 'words': words }

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

  return render(request, 'twowords/detail.html', {
    'word': word,
  })


@login_required
def add_comment(request, word_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.word_id = word_id
    new_comment.save()
  return redirect('detail', word_id=word_id)

