from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_badge', 'updated_at', 'image_preview')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at', 'preview_image')
    
    fieldsets = (
        ('📝 Blog Content', {
            'fields': ('title', 'description', 'image', 'preview_image')
        }),
        ('⏰ Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            html = f'<img src="{obj.image.url}" class="blog-list-thumbnail" />'
            return mark_safe(html)
        return '-'
    image_preview.short_description = 'Preview'
    
    def preview_image(self, obj):
        if obj.image:
            html = f'<img src="{obj.image.url}" class="blog-preview-image" />'
            return mark_safe(html)
        return '⚠️ No image uploaded'
    preview_image.short_description = 'Image Preview'
    
    def date_badge(self, obj):
        html = f"<span class='blog-date-badge'>{obj.created_at.strftime('%d %b %Y')}</span>"
        return mark_safe(html)
    date_badge.short_description = 'Published'
