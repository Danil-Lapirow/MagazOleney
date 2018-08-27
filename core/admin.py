from django.contrib import admin
from core.models import Post


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'owner', 'is_published', 'published_at'
    )
    search_fields = (
        'title', 'text'
    )


admin.site.register(Post, PostAdmin)
