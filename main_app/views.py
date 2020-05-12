from django.shortcuts import render 

# Create your views here.

def about(request):
  return render(request, 'about.html')

def words(request):
  return render(request, 'twowords/index.html')