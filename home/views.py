from django.shortcuts import render
from blog.models import BlogPost
from home.models import Portfolio, Gallery
from forms_app.models import TOPIC_CHOICES

def index(request):
    blog_posts = BlogPost.objects.all()[:6]
    portfolios = Portfolio.objects.all()[:6]
    context = {
        'blog_posts': blog_posts,
        'portfolios': portfolios,
        'services': [
            'Residential Design',
            'Commercial Design',
            'Hospitality Design',
            'Space Planning',
            'Working Drawing',
            '3D Visualization',
            'Renovation & Remodeling',
            'Interior Styling',
        ]
    }
    return render(request, 'index.html', context)

def gallery(request):
    gallery_items = Gallery.objects.all()
    
    context = {
        'gallery_items': gallery_items,
        'gallery_count': gallery_items.count(),
    }
    return render(request, 'gallery.html', context)
