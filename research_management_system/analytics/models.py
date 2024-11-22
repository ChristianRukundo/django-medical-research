from django.db import models

class ResearchStatistics(models.Model):
    research_title = models.CharField(max_length=255)
    views_count = models.IntegerField(default=0)
    downloads_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.research_title
