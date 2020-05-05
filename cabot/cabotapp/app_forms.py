from django import forms

#from models import Service, Issue

'''
class IssueReportForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ("reporter", "reporter_email", "service", "complain")
'''

class IssueReport(forms.Form):
    name= forms.CharField(label = "Your name   ", max_length=30)
    email= forms.EmailField(label = "Your Email   ")
    complain= forms.CharField(widget=forms.Textarea, label = "Issue Details")
