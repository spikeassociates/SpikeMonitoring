from django import forms

from models import Issue

class IssueReportForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ("reporter", "reporter_email", "service", "complain")