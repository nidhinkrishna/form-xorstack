from .models import FormSam
from django import forms

class SampleForm(forms.ModelForm):
    class Meta:
        model = FormSam
        fields = '__all__'