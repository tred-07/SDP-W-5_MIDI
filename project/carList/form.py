from django import forms
from .models import CarList

class carlist(forms.ModelForm):
    class Meta:
        model=CarList
        fields='__all__'