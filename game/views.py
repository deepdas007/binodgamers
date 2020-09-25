from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from game.models import blogPost


def home(request):
    return render(request, 'game/home.html')


def news(request):
    blog_list = blogPost.objects.all()
    paginator = Paginator(blog_list, 3)  # Show 3 posts per page

    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    context = {
        'blogs': blogs,
    }
    return render(request, 'game/news.html', context)


def newsPage(request):
    return render(request, 'game/newsPage.html')
