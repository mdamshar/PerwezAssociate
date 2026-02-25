from django import template

register = template.Library()

@register.filter
def youtube_id(url):
    """Extract YouTube video ID from URL"""
    if 'youtu.be' in url:
        return url.split('youtu.be/')[-1].split('?')[0]
    elif 'youtube.com' in url:
        return url.split('v=')[-1].split('&')[0]
    return ''

@register.filter
def vimeo_id(url):
    """Extract Vimeo video ID from URL"""
    if 'vimeo.com' in url:
        return url.split('/')[-1].split('?')[0]
    return ''

@register.filter
def is_youtube(url):
    """Check if URL is YouTube"""
    return 'youtube.com' in url or 'youtu.be' in url

@register.filter
def is_vimeo(url):
    """Check if URL is Vimeo"""
    return 'vimeo.com' in url
