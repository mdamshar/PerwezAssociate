from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Portfolio, Gallery

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'count_projects')
    search_fields = ('name',)
    
    fieldsets = (
        ('📂 Category Information', {
            'fields': ('name', 'description')
        }),
    )
    
    def count_projects(self, obj):
        count = obj.portfolios.count()
        return f"<span style='background: #667eea; color: white; padding: 3px 8px; border-radius: 5px;'>{count} projects</span>"
    count_projects.short_description = 'Projects'
    count_projects.allow_tags = True

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_badge', 'image_preview')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'preview_image')
    
    fieldsets = (
        ('🏗️ Project Details', {
            'fields': ('title', 'description', 'category', 'image', 'preview_image')
        }),
        ('⏰ Timestamp', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="150" style="border-radius: 8px;"/>'
        return '❌ No image'
    image_preview.allow_tags = True
    image_preview.short_description = 'Thumbnail'
    
    def preview_image(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="400" style="border-radius: 10px; box-shadow: 0 5px 15px rgba(0,0,0,0.2);"/>'
        return '⚠️ No image uploaded'
    preview_image.allow_tags = True
    preview_image.short_description = 'Full Preview'
    
    def date_badge(self, obj):
        return f"<span style='background: #764ba2; color: white; padding: 3px 8px; border-radius: 5px;'>{obj.created_at.strftime('%d %b %Y')}</span>"
    date_badge.short_description = 'Created'
    date_badge.allow_tags = True

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_thumbnail', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at', 'image_preview')
    
    fieldsets = (
        ('📸 Gallery Image', {
            'fields': ('title', 'image')
        }),
        ('👀 Preview', {
            'fields': ('image_preview',),
        }),
        ('⏰ Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def image_thumbnail(self, obj):
        if obj.image:
            html = f'<img src="{obj.image.url}" width="50" height="50" style="border-radius: 4px; object-fit: cover;" />'
            return mark_safe(html)
        return '❌ No image'
    image_thumbnail.short_description = 'Thumbnail'
    
    def image_preview(self, obj):
        if obj.image:
            html = f'<img src="{obj.image.url}" width="400" style="border-radius: 10px; box-shadow: 0 5px 15px rgba(0,0,0,0.2);" />'
            return mark_safe(html)
        return '⚠️ No image uploaded'
    image_preview.short_description = 'Full Preview'

