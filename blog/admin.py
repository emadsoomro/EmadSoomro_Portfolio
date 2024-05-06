from django.contrib import admin

from blog.models import service
from blog.models import Contact_Me
from blog.models import skills

class serAdmin(admin.ModelAdmin):
    list_display = ('service_icon','service_title','service_des')

admin.site.register(service, serAdmin)

class Contact_Admin(admin.ModelAdmin):
    list_display = ('name','email','subject','msg')

admin.site.register(Contact_Me, Contact_Admin)

class skills_Admin(admin.ModelAdmin):
    list_display = ('skill_icon','skill_icon_style','skill_title')

admin.site.register(skills, skills_Admin)
# Register your models here.
