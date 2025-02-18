from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'email', 'message']

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'py-2 border bg-[#274F74] border-white rounded px-2 text-base text-white focus:outline-none',
                'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={
                'class': 'py-2 border bg-[#274F74] border-white rounded px-2 text-base text-white focus:outline-none',
                'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={
                'class': 'py-2 border bg-[#274F74] border-white rounded px-2 text-base text-white focus:outline-none',
                'placeholder': 'example@gmail.com'}),
            'message': forms.Textarea(attrs={
                'class': 'py-2 border bg-[#274F74] border-white rounded px-2 text-base text-white focus:outline-none',
                'placeholder': 'I want to know about...', 'rows': 5}),
        }
