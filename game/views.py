from django.shortcuts import render
from django.http import HttpResponse
# from game.models import Question


def home(request):
    return render(request, 'game/home.html')


def news(request):
    return render(request, 'game/news.html')


def newsPage(request):
    return render(request, 'game/newsPage.html')
