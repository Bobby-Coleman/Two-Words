from django.shortcuts import render 

# Create your views here.

def home(request):
  return render(request, 'home.html')

def words(request):
  return render(request, 'twowords/index.html')