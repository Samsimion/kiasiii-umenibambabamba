from django import forms
from .models import PrimarySchool, HighSchool

class PrimarySchoolForm(forms.ModelForm):
    class Meta :
        model = PrimarySchool
        fields = '__all__'

class HighSchoolForm(forms.ModelForm):
    class Meta:
        model = HighSchool
        fields = '__all__'