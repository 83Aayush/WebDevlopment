"""
Project Title : Contact Management System
Name         : [Your Name]
Date         : 2025
Description  : Django forms for Contact model
               Forms handle validation automatically — no need to write
               if/else checks manually for each field.
"""

from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    ContactForm is linked directly to our Contact model.
    Django generates the form fields from the model automatically.
    We just customize labels and widgets (how they look in HTML).
    """

    class Meta:
        model = Contact         # Which model does this form work with?
        fields = ['name', 'phone', 'email', 'address']  # Which fields to show

        # Labels — what the user sees next to each input box
        labels = {
            'name': 'Full Name',
            'phone': 'Phone Number',
            'email': 'Email Address',
            'address': 'Address (Optional)',
        }

        # Widgets — HTML attributes like placeholder text and CSS classes
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Ravi Kumar',
                'autofocus': True,
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 9876543210',
                'maxlength': '15',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. ravi@example.com',
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Street, City, State (optional)',
                'rows': 3,
            }),
        }

    def clean_phone(self):
        """
        Custom validation for phone number.
        Django calls clean_<fieldname>() automatically during form validation.
        """
        phone = self.cleaned_data.get('phone', '').strip()

        # Remove spaces, dashes, brackets for clean check
        digits_only = phone.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')

        # Must have at least 7 digits and at most 15
        if not digits_only.lstrip('+').isdigit():
            raise forms.ValidationError("Phone number should contain only digits, +, -, spaces.")

        if len(digits_only.lstrip('+')) < 7:
            raise forms.ValidationError("Phone number is too short. Enter at least 7 digits.")

        return phone

    def clean_name(self):
        """Validate that name is not just whitespace."""
        name = self.cleaned_data.get('name', '').strip()
        if not name:
            raise forms.ValidationError("Name cannot be blank.")
        return name
