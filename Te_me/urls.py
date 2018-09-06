"""Te_me URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from django.views.generic import TemplateView
from django.views.static import serve

from Te_me.settings import MEDIA_ROOT
# 生产环境对 静态文件 访问处理的支持
# from Te_me.settings import STATIC_ROOT

from blog.views import GlobalSearchView

urlpatterns = [
    # django默认管理后台
    path('admin/', admin.site.urls),

    # 自定义管理后台
    # path('dashboard/', include('dashboard.urls'), name='dashboard'),

    # 首页、欢迎页面，俗称index页面

    # All kinds of APP's urls
    # About - Page
    url(r'about/', TemplateView.as_view(template_name='layouts/general/about.html'), name='about'),

	# Blog
    url('blog/', include('blog.urls'), name='blog'),

    # 网站基本功能依赖
    # 配置静态图片上传的加载处理
    url(r'files/img/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

    # 配置 静态文件 访问处理函数 - 用于生产环境
    # url(r'static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT}),

]

# 配置全局 404 ERROR 错误页面

# 配置全局 500 ERROR 错误页面
