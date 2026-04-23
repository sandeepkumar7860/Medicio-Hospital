from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'date', 'department', 'doctor', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email', 'required': True}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone', 'required': True}),
            'date': forms.DateTimeInput(attrs={'class': 'form-control datepicker', 'type': 'datetime-local', 'placeholder': 'Appointment Date', 'required': True}),
            'department': forms.Select(attrs={'class': 'form-select', 'required': True}, choices=[
                ('', 'Select Department'),
                ('Cardiology', 'Cardiology'),
                ('Neurology', 'Neurology'),
                ('Emergency Department (ED)', 'Emergency Department (ED)'),
            ]),
            'doctor': forms.Select(attrs={'class': 'form-select', 'required': True}, choices=[
                ('', 'Select Doctor'),
                ('Dr Batra', 'Dr Batra'),
                ('Dr Shahni', 'Dr Shahni'),
                ('Dr Mohan', 'Dr Mohan'),
            ]),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Message (Optional)'}),
        }