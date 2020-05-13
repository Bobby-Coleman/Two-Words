from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import requests 
import json
# from random_word import RandomWords


def words(request):
  r = requests.get("https://random-word-api.herokuapp.com/word?number=2").json()
  word_one = r[0]
  word_two = r[1]
  try:
    words = json.loads(r.content)

  except Exception as e:
    words = "Error data not loading"

  words = {
    'word_one' : word_one,
    'word_two' : word_two,
  }

  context = {'words' : words }

  return render (request, 'twowords/index.html', context)


# def words(request):
#   r = requests.get("https://random-word-api.herokuapp.com/word?number=2")
#   try:
#     api = json.loads(r.content)
#   except Exception as e:
#     api = "Error data not loading"

#   return render (request, 'twowords/index.html', {'api' : api})


# def get_words(req):
#   print(r)
# r = RandomWords()

# def get_words():
  # print(r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb", minCorpusCount=1, maxCorpusCount=10, minDictionaryCount=1, maxDictionaryCount=10, minLength=5, maxLength=10))

# r = requests.get("https://random-word-api.herokuapp.com/word?number=2")
# if r.status_code != 200:
#     # This means something went wrong.
#     raise ApiError('GET /tasks/ {}'.format(r.status_code))
# for todo_item in r.json():
#     print('{} {}'.format(todo_item['id'], todo_item['summary'])


def about(request):
  return render(request, 'about.html')

# @login_required
# def words(request):
#   return render(request, 'twowords/index.html')

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