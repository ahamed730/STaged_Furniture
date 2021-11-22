from django import forms
from django.db.models import fields
from .models import Customer, Address, Category, Furniture, TicketItem


class FurnitureForm(forms.ModelForm):
    class Meta:
        model = Furniture
        exclude = ['category']


class TicketItemForm(forms.ModelForm):
    class Meta:
        model = TicketItem
        exclude = ['None']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name','last_name','phone_number', 'email']
       

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street_address','city', 'state' ]
