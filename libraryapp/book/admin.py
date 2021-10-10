from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db.models import fields

# Register your models here.

User=get_user_model()
class MainUserAdmin(admin.ModelAdmin):
    search_fields = ['email']
    list_display=('email','timestamp')
    list_filter=('timestamp',)
    editable_list = ['image']

admin.site.register(Book)
admin.site.register(User,MainUserAdmin)

admin.site.unregister(Group)

# Register your models here.
admin.site.site_header="ToDo App"
