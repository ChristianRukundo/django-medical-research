from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import ResearchProject, ResearchData
from .forms import ResearchProjectForm, ResearchDataForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ResearchProjectForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


@login_required
def view_research_projects(request):
    research_projects = ResearchProject.objects.filter(user=request.user)
    return render(request, 'research_list.html', {'research_projects': research_projects})

@login_required
def create_research_project(request):
    if request.method == 'POST':
        form = ResearchProjectForm(request.POST)
        if form.is_valid():
            research_project = form.save(commit=False)
            research_project.user = request.user
            research_project.save()
            messages.success(request, 'Research project created successfully!')
            return redirect('research_projects_list')
    else:
        form = ResearchProjectForm()
    return render(request, 'research_form.html', {'form': form})


@login_required
def update_research_project(request, pk):
    research_project = get_object_or_404(ResearchProject, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ResearchProjectForm(request.POST, instance=research_project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Research project updated successfully!')
            return redirect('view_research_projects')
    else:
        form = ResearchProjectForm(instance=research_project)
    return render(request, 'research_form.html', {'form': form})

# Delete a research project
@login_required
def delete_research_project(request, pk):
    research_project = get_object_or_404(ResearchProject, pk=pk, user=request.user)
    if request.method == 'POST':
        research_project.delete()
        messages.success(request, 'Research project deleted successfully!')
        return redirect('research_projects_list')
    return render(request, 'research_confirm_delete.html', {'research_project': research_project})

