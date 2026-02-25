from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_list(request):
    blogs = BlogPost.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog/blog_list.html', context)

def blog_detail(request, pk):
    blog = get_object_or_404(BlogPost, pk=pk)
    other_blogs = BlogPost.objects.exclude(pk=pk)[:3]
    context = {
        'blog': blog,
        'other_blogs': other_blogs
    }
    return render(request, 'blog/blog_detail.html', context)
