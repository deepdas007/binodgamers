# Generated by Django 3.0.6 on 2020-09-24 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=200, verbose_name='Post title')),
                ('post_by', models.CharField(max_length=200, verbose_name='Post by')),
                ('post_para_1', models.CharField(max_length=2000, verbose_name='Post paragraph 1')),
                ('post_para_2', models.CharField(max_length=2000, verbose_name='Post paragraph 2')),
                ('post_para_3', models.CharField(max_length=2000, verbose_name='Post paragraph 3')),
                ('post_quote', models.CharField(max_length=2000, verbose_name='Post Quote')),
                ('post_quote_by', models.CharField(max_length=200, verbose_name='Post Quote by')),
                ('last_para_1', models.CharField(max_length=2000, verbose_name='Last paragraph 2')),
                ('last_para_2', models.CharField(max_length=2000, verbose_name='Last paragraph 3')),
                ('pub_date', models.DateTimeField(verbose_name='Date published')),
            ],
        ),
    ]
