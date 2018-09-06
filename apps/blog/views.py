from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.http import HttpResponse
from django.db.models import Q
from Te_me.settings import DATABASES

import redis

from .models import BlogArticles
# Create your views here.

# 初始化 Redis 数据库连接
r = redis.StrictRedis(host=DATABASES['redis']['REDIS_HOST'],
                      port=DATABASES['redis']['REDIS_PORT'],
                      db=DATABASES['redis']['REDIS_DB'])


class GlobalSearchView(View):
    # get请求
    def get(self, request):
        all_articles = BlogArticles.objects.all().order_by("-add_time")

        keyword = request.GET.get("keyword", "")
        if keyword:
            all_results = all_articles.filter(Q(title__icontains=keyword) | Q(author__icontains=keyword) | Q(tags__icontains=keyword) | Q(content__icontains=keyword))

        return