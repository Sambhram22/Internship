from django import forms
from datetime import date

class PromotionEligibilityForm(forms.Form):
    EMPLOYEE_CHOICES = [
        ('E001', 'E001 - Rahul Shetty'),
        ('E002', 'E002 - Priyanka Patel'),
        ('E003', 'E003 - Rohan Roy'),
    ]
    employee_id = forms.ChoiceField(choices=EMPLOYEE_CHOICES, label="Employee ID")
    date_of_joining = forms.DateField(
        label="Date of Joining",
        widget=forms.DateInput(attrs={'type': 'date'}),
    )
