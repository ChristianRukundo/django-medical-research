from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
class ResearchProject(models.Model):
    RESEARCH_FIELDS = [
        ('Science', 'Science'),
        ('Technology', 'Technology'),
        ('Mathematics', 'Mathematics'),
        ('Engineering', 'Engineering'),
        ('Social Sciences', 'Social Sciences'),
        ('Arts', 'Arts'),
    ]
    title = models.CharField(max_length=255)
    field = models.CharField(max_length=100, choices=RESEARCH_FIELDS,default="life")
    summary = models.TextField()
    location = models.CharField(max_length=100,default="earth")
    date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Use custom user model

    def __str__(self):
        return self.title

class ResearchData(models.Model):
    project = models.ForeignKey(ResearchProject, on_delete=models.CASCADE)
    data_file = models.FileField(upload_to='research_data/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Data for {self.project.title}"
