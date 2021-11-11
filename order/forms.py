from django import forms
from django.db.models import fields
from .models import Customer, Address, Category, Furniture


class FurnitureForm(forms.ModelForm):
    class Meta:
        model = Furniture
        exclude = ['None',]