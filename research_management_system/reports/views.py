from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
# from research_data.models import ResearchProject
from .models import Report
from django.http import HttpResponse

def report_list(request):
    return HttpResponse("This is the report list page.")

def report_detail(request, id):
    return HttpResponse(f"This is the detail page for report {id}.")
