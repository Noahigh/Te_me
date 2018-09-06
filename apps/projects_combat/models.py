from django.db import models
from datetime import datetime

# Create your models here.


# ProjectsProfile 项目详情
class ProjectsProfile(models.Model):
    name = models.CharField(max_length=100, verbose_name=u"项目名称")
    category = models.CharField(max_length=20, verbose_name=u"项目分类")
    profile = models.CharField(max_length=300, verbose_name=u"项目简介")
    details = models.TextField(verbose_name=u"项目详情")
    requirements = models.TextField(verbose_name=u"技术要求")
    skills_map = models.ImageField(default=u"img/projects_profile/skills_map/default.jpg", max_length=100, null=True, blank=True, verbose_name=u"技能图谱")
    reference_case = models.CharField(max_length=300, verbose_name=u"参考案例")
    recommended = models.IntegerField(default=0, choices=((0, u"未评级"), (1, u"一颗星"), (2, u"二颗星"), (3, u"三颗星"), (4, u"四颗星"), (5, u"五颗星")), verbose_name=u"推荐指数")
    create_time = models.DateTimeField(default=datetime.now, verbose_name=u"项目详情增加时间")
    update_time = models.DateTimeField(default=datetime.now, verbose_name=u"项目详情更新时间")

    class Meta:
        verbose_name = u"项目详情"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


