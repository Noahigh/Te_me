from datetime import datetime

from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.


# UserProfile 用户信息
# 继承django抽象用户类
class UserProfile(AbstractUser):
    nickname = models.CharField(default="", max_length=50, verbose_name=u"用户昵称")
    gender = models.CharField(default="female", max_length=6, choices=(("male", u"男"), ("female", u"女")), verbose_name=u"性别")
    birthday = models.DateField(null=True, blank=True, verbose_name=u"用户生日")
    portrait = models.ImageField(default=u"img/users/portrait/default.jpg", max_length=100, null=True, blank=True, upload_to=u"img/users/portrait/%Y/%m", verbose_name=u"用户头像")
    # 第三方登录
    # qq_related =
    # wechat_related =
    # weibo_related =
    # ali_related =
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u"用户信息增加时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u"用户信息更新时间")

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
