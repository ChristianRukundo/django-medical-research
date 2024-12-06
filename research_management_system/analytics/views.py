from django.db.models import Count
from django.db.models.functions import TruncDate
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from research_data.models import ResearchProject


@login_required
def dashboard(request):
    user = request.user

    user_projects = ResearchProject.objects.filter(user=user)
    total_projects = user_projects.count()

    date_stats = (
        user_projects.annotate(project_date=TruncDate('date'))
        .values('project_date')
        .annotate(project_count=Count('id'))
        .order_by('project_date')
    )

    field_stats = (
        user_projects.values('field')
        .annotate(project_count=Count('id'))
        .order_by('-project_count')
    )

    dates = [stat['project_date'].strftime('%Y-%m-%d') for stat in date_stats]
    date_counts = [stat['project_count'] for stat in date_stats]

    fields = [stat['field'] for stat in field_stats]
    field_counts = [stat['project_count'] for stat in field_stats]

    context = {
        'total_projects': total_projects,
        'dates': dates,
        'date_counts': date_counts,
        'fields': fields,
        'field_counts': field_counts,
    }
    return render(request, 'dashboard.html', context)
