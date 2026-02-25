from django.urls import path
from . import views

app_name = 'forms'

urlpatterns = [
    path('quote/', views.get_quote, name='quote'),
    path('feedback/', views.submit_feedback, name='feedback'),
]
