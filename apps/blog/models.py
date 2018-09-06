from datetime import datetime

from django.db import models
from django.utils import timezone

from users.models import UserProfile

# Create your models here.


# Blog Articles 文章表
class BlogArticles(models.Model):
    title = models.CharField(max_length=300, verbose_name=u"文章标题")
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"文章作者")
    tags = models.CharField(max_length=100, verbose_name=u"文章分类")
    content = models.TextField(verbose_name=u"文章内容")
    click_nums = models.IntegerField(default=0, verbose_name=u"文章阅读数")
    like_nums = models.IntegerField(default=0, verbose_name=u"文章点赞数")
    create_time = models.DateTimeField(default=timezone.now, verbose_name=u"文章添加时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u"文章更新时间")

    class Meta:
        verbose_name = u"文章详情"
        verbose_name_plural = verbose_name
        # 按publish的倒序来显示
        ordering = ("-create_time",)

    def __str__(self):
        return self.title


# ArticlesTags 文章标签表
class ArticlesTags(models.Model):
    name = models.CharField(default="", max_length=20, verbose_name=u"标签名称")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name=u"创建标签的用户")
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u"标签创建时间")

    class Meta:
        verbose_name = u"文章标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# ATRelationship 文章和标签关系表 - 一对多关系
class ATRelationship(models.Model):
    article_id = models.ForeignKey(BlogArticles, on_delete=models.CASCADE, verbose_name=u"文章ID")
    tags_ids = models.CharField(max_length=100, verbose_name=u"标签ID集合")

    class Meta:
        verbose_name = u"文章和标签关系"
        verbose_name_plural = verbose_name

    def __str__(self):
        return u"文章和标签关系"
