from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish')
    list_filter = ('created', 'publish')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('-publish',)