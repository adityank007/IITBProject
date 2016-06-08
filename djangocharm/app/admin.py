from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
from django.contrib.auth.models import User
from .models import UserInfo
from .models import addtheme
from .models import addsubject

class AdminInfo(admin.ModelAdmin):
	list_display = ["__str__"]
	class Meta:
		model=UserInfo

class UserInline(admin.StackedInline):
	model=UserInfo
	can_delete=False
	verbose_name_plural='userinfo'

class UserAdmin(BaseUserAdmin):
	inlines= (UserInline,)




admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(addtheme)
admin.site.register(addsubject)

