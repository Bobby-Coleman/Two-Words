from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import requests 
import json
# from random_word import RandomWords
from . models import Word

@login_required
def words(request):
  r = requests.get("https://random-word-api.herokuapp.com/word?number=2").json()

  word_one = r[0]
  word_two = r[1]

  if request.method == "GET":
    try:
      words = json.loads(r.content)

    except Exception as e:
      words = "Error data not loading"

      words = {
      'word_one' : word_one,
      'word_two' : word_two,
     }

  if request.method == 'POST':
      Word.objects.create(word_one = word_one, word_two = word_two)

  context = {'words' : words }

  return render (request, 'twowords/index.html', context)


@login_required
def words_list(request):
  # words = Word.objects.filter(user=request.user)
  # words = Word.objects.all()
  return render(request, 'twowords/list.html', )

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