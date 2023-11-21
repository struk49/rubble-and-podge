from django import forms

from .models import Contact


class ContavtForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'message']