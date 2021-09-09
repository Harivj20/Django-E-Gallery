from django import forms
from django.forms import fields, models
from .models import Photo,Category,Theme

class Form(forms.ModelForm):
    class Meta:
        model=Photo
        fields="__all__"

class Forms(forms.ModelForm):
    class Meta:
        model=Category
        fields="__all__"     

class Themeform(forms.ModelForm):           
    class Meta:
        model=Theme
        fields='__all__'


        