# Generated by Django 3.0.6 on 2020-09-30 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20200930_0922'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='post_overview',
            field=models.CharField(blank=True, max_length=400, verbose_name='Post overview'),
        ),
    ]
