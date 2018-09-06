from django.contrib import admin

from .models import UserProfile

# Register your models here.


# UsersProfileAdmin 用户信息注册到后台管理系统
class UsersProfileAdmin(admin.ModelAdmin):
    list_display = ("username", "nickname", "gender", "birthday", "portrait", "create_time", "update_time")
    list_filter = ("username", "update_time", "update_time", "gender")
    search_fields = ("username", "nickname")
    date_hierarchy = "create_time"
    ordering = ["update_time", "create_time"]


admin.site.register(UserProfile, UsersProfileAdmin)
