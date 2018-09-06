# Generated by Django 2.0.7 on 2018-08-06 19:22

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlesTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, verbose_name='标签名称')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='标签创建时间')),
            ],
            options={
                'verbose_name': '文章标签',
                'verbose_name_plural': '文章标签',
            },
        ),
        migrations.CreateModel(
            name='ATRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags_ids', models.CharField(max_length=100, verbose_name='标签ID集合')),
            ],
            options={
                'verbose_name': '文章和标签关系',
                'verbose_name_plural': '文章和标签关系',
            },
        ),
        migrations.CreateModel(
            name='BlogArticles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='文章标题')),
                ('tags', models.CharField(max_length=100, verbose_name='文章分类')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('click_nums', models.IntegerField(default=0, verbose_name='文章阅读数')),
                ('like_nums', models.IntegerField(default=0, verbose_name='文章点赞数')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='文章添加时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='文章更新时间')),
            ],
            options={
                'verbose_name': '文章详情',
                'verbose_name_plural': '文章详情',
                'ordering': ('-create_time',),
            },
        ),
    ]
