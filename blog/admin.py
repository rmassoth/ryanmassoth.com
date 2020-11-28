from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    date_heirarchy = '-created_at'
    list_display = ('created_at', 'title', 'last_updated', 'published',)
    list_filter = ('created_at', 'published',)
