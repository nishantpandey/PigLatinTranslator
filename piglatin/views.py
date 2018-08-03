from django.http import HttpResponse
from django.shortcuts import render


def home(request):
	return render(request,'home.html')


def translate(request):
  old_value = request.GET['textbox'].lower()
  new_value = old_value + "NEW"
  return render(request,'translate.html',{'old':old_value, 'new':new_value})

def about(request):
	return render(request,'about.html')
