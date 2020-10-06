from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from game.models import blogpost


def home(request):
    return render(request, 'game/home.html')


def news(request):
    blog_list = blogpost.objects.order_by('-pub_date')
    paginator = Paginator(blog_list, 3)  # Show 3 posts per page
    page = request.GET.get('page')
    blogs = paginator.get_page(page)
    next_to_next = blogs.number + 2
    has_next_to_next = False
    is_last_page = False
    if next_to_next <= blogs.paginator.num_pages:
        has_next_to_next = True
    if blogs.number == blogs.paginator.num_pages:
        is_last_page = True

    context = {
        'blogs': blogs,
        'next_to_next': next_to_next,
        'has_next_to_next': has_next_to_next,
        'is_last_page': is_last_page,
    }
    return render(request, 'game/news.html', context)


def newsPage(request, blogpost_id):
    try:
        blog = blogpost.objects.get(pk=blogpost_id)
    except blogpost.DoesNotExist:
        raise Http404("Blog does not exist")

    context = {
        'blog': blog,
    }

    return render(request, 'game/newsPage.html', context)
