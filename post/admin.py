from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','content','publishing_dttm']
    search_fields = ['title']
    list_filter = ['title','publishing_dttm']