from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import index, gallery

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('gallery/', gallery, name='gallery'),
    path('blog/', include('blog.urls', namespace='blog')),
    path('forms/', include('forms_app.urls', namespace='forms')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
