from django.contrib import admin
from .models import Control


# Register your models here.
@admin.register(Control)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
