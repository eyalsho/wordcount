from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html')


def count(request):
    message = request.GET['textinput']
    num_of_words = 0
    if message != None:
        num_of_words = len(message.split())
    return render(request, 'count_result.html', {'sentence':message, 'number_of_words':num_of_words})


def about(request):
    return render(request, 'about.html')
