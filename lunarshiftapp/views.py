from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from models import Employee

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")
    #latest_question_list = 
    #context = 
    #return render(request, 'polls/index.html', context)