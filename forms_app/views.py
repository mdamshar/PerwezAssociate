from django.shortcuts import render, redirect
from django.contrib import messages
from .models import QuoteRequest, Feedback
from .forms import QuoteRequestForm, FeedbackForm

def get_quote(request):
    if request.method == 'POST':
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Quote request submitted successfully! We will contact you soon.')
            return redirect('index')
    else:
        form = QuoteRequestForm()
    
    context = {'form': form}
    return render(request, 'forms/quote_form.html', context)

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your feedback!')
            return redirect('index')
    else:
        form = FeedbackForm()
    
    context = {'form': form}
    return render(request, 'forms/feedback_form.html', context)
