from django import forms
from .models import ResearchProject, ResearchData

class ResearchProjectForm(forms.ModelForm):
    class Meta:
        model = ResearchProject
        fields = ['title', 'field', 'summary', 'location', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class ResearchDataForm(forms.ModelForm):
    class Meta:
        model = ResearchData
        fields = ['data_file']
