from django.db.models import Count
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from research_data.models import ResearchProject



@login_required
def dashboard(request):
    # Aggregate the number of projects per user
    user_stats = (
        ResearchProject.objects.values('user__username')
        .annotate(project_count=Count('id'))
        .order_by('-project_count')
    )

    # Prepare data for the graph
    usernames = [stat['user__username'] for stat in user_stats]
    project_counts = [stat['project_count'] for stat in user_stats]

    context = {
        'usernames': usernames,
        'project_counts': project_counts,
    }
    return render(request, 'analytics/dashboard.html', context)
