from django.db import models
from research_data.models import ResearchProject


class Report(models.Model):
    project = models.ForeignKey(ResearchProject, on_delete=models.CASCADE)
    report_file = models.FileField(upload_to='reports/')
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report for {self.project.title}"
