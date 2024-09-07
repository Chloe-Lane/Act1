from django import forms
from .models import Inquire

class InquireForm(forms.ModelForm):
    class Meta:
        model = Inquire
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'subject': forms.TextInput(attrs={'placeholder': 'Enter the subject'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter your message', 'rows': 4}),
        }

    # Validate name to ensure it contains only letters and spaces
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.replace(' ', '').isalpha():
            raise forms.ValidationError("Name can only contain letters and spaces.")
        return name.strip()

    # You can add additional custom validations for subject or message if needed
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 10:
            raise forms.ValidationError("Message must be at least 10 characters long.")
        return message.strip()
