from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('news', views.news, name='news'),
    path('news/<int:blogpost_id>', views.newsPage, name='newsPage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
