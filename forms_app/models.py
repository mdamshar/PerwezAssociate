from django.db import models

TOPIC_CHOICES = [
    ('residential', 'Residential Design'),
    ('commercial', 'Commercial Design'),
    ('hospitality', 'Hospitality Design'),
    ('space_planning', 'Space Planning'),
    ('working_drawing', 'Working Drawing'),
    ('3d_visualization', '3D Visualization'),
    ('renovation', 'Renovation & Remodeling'),
    ('interior_styling', 'Interior Styling'),
    ('project_planning', 'Project Planning'),
    ('general_contracting', 'General Contracting'),
]

class QuoteRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('deleted', 'Deleted'),
    ]
    
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    topic = models.CharField(max_length=50, choices=TOPIC_CHOICES)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.topic}"
    
    class Meta:
        ordering = ['-created_at']


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Feedback from {self.name}"
    
    class Meta:
        ordering = ['-created_at']
