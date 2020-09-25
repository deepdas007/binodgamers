import datetime

from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class blogPost(models.Model):
    post_title = models.CharField('Post title', max_length=200)
    post_by = models.CharField('Post by', max_length=200)
    head_image = models.ImageField(upload_to='images/', blank=True)
    post_para_1 = models.CharField('Post paragraph 1', max_length=2000)
    post_content = RichTextField(blank=True, null=True)
    post_para_2 = models.CharField(
        'Post paragraph 2', max_length=2000, blank=True)
    post_para_3 = models.CharField(
        'Post paragraph 3', max_length=2000, blank=True)
    post_quote = models.CharField('Post Quote', max_length=2000, blank=True)
    post_quote_by = models.CharField(
        'Post Quote by', max_length=200, blank=True)
    last_para_1 = models.CharField(
        'Last paragraph 2', max_length=2000, blank=True)
    last_para_2 = models.CharField(
        'Last paragraph 3', max_length=2000, blank=True)
    pub_date = models.DateTimeField('Date published')

    def __str__(self):
        return self.post_title

    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=2)
        # timezone.now() - datetime.timedelta(days=1) means 1 day back of timezone.now day
        # self.pub_date >= timezone.now() - datetime.timedelta(days=1) the Question.was_published_recently() method returns True if the Question was published within the last day
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
