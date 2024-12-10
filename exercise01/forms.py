from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    date_of_birth = forms.DateField(label="Date of Birth", widget=forms.DateInput(attrs={'type': 'date'}))
    address = forms.CharField(label="Address", widget=forms.Textarea)
    contact_number = forms.CharField(label="Contact Number", max_length=15)
    email_id = forms.EmailField(label="Email ID")
    marks_english = forms.FloatField(label="Marks in English")
    marks_physics = forms.FloatField(label="Marks in Physics")
    marks_chemistry = forms.FloatField(label="Marks in Chemistry")
