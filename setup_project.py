#!/usr/bin/env python
"""
Django setup script for Perwez Associate
Creates superuser and loads initial data
"""

import os
import django
import sys

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'perwez_config.settings')
django.setup()

from django.contrib.auth.models import User
from home.models import Category
from blog.models import BlogPost

DEFAULT_ADMIN_USERNAME = 'shariqueperwez'
DEFAULT_ADMIN_EMAIL = 'shariqueperwez3@gmail.com'
DEFAULT_ADMIN_PASSWORD = 'perwez@#belA786'

def setup_superuser():
    """Create superuser if not exists"""
    admin_user = User.objects.filter(username=DEFAULT_ADMIN_USERNAME).first()
    if not admin_user:
        User.objects.create_superuser(
            DEFAULT_ADMIN_USERNAME,
            DEFAULT_ADMIN_EMAIL,
            DEFAULT_ADMIN_PASSWORD,
        )
        print(f"✓ Superuser created! (username: {DEFAULT_ADMIN_USERNAME})")
    else:
        admin_user.email = DEFAULT_ADMIN_EMAIL
        admin_user.is_staff = True
        admin_user.is_superuser = True
        admin_user.set_password(DEFAULT_ADMIN_PASSWORD)
        admin_user.save()
        print(f"✓ Superuser updated! (username: {DEFAULT_ADMIN_USERNAME})")

def setup_categories():
    """Create service categories"""
    categories = [
        'Residential Design',
        'Commercial Design',
        'Hospitality Design',
        'Space Planning',
        'Working Drawing',
        '3D Visualization',
        'Renovation & Remodeling',
        'Interior Styling',
    ]
    
    for category_name in categories:
        Category.objects.get_or_create(name=category_name)
    
    print(f"✓ {len(categories)} categories created/updated")

def setup_sample_blog():
    """Create sample blog post"""
    blog_exists = BlogPost.objects.filter(title__icontains='Welcome').exists()
    
    if not blog_exists:
        BlogPost.objects.create(
            title='Welcome to Perwez Associate',
            description='Welcome to our blog! Here we share our latest projects, design tips, and industry insights. Stay tuned for more exciting updates about construction and interior design trends.'
        )
        print("✓ Sample blog post created")
    else:
        print("✓ Sample blog post already exists")

if __name__ == '__main__':
    print("\n" + "="*50)
    print("Setting up Perwez Associate...")
    print("="*50 + "\n")
    
    try:
        setup_superuser()
        setup_categories()
        setup_sample_blog()
        print("\n" + "="*50)
        print("Setup completed successfully!")
        print("="*50)
        print("\nNext steps:")
        print("1. Run: python manage.py runserver")
        print("2. Visit: http://localhost:8000")
        print("3. Admin: http://localhost:8000/admin")
        print(f"   (username: {DEFAULT_ADMIN_USERNAME}, password: {DEFAULT_ADMIN_PASSWORD})\n")
    except Exception as e:
        print(f"✗ Error during setup: {e}")
        sys.exit(1)
