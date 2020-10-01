import datetime

from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField


class blogpost(models.Model):
    post_title = models.CharField('Post title', max_length=200)
    post_by = models.CharField('Post by', max_length=200)
    head_image = models.ImageField(upload_to='images/', blank=True)
    post_overview = models.CharField(
        'Post overview', max_length=400, blank=True)
    post_content = RichTextField(blank=True, null=True)

    pub_date = models.DateTimeField('Date published')

    def __str__(self):
        return self.post_title
