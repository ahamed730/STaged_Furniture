from django.shortcuts import render
from order.models import Category
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, FormView
from .forms import FurnitureForm
from .models import Customer, Address, Furniture
from django.urls import reverse_lazy


# Create your views here.
def furnitureform(request):
    if request.method == "POST":
        furniture_form = FurnitureForm(data=request.POST)


        if furniture_form.is_valid():

            furniture = furniture_form.save(commit=False) 
            category_field = request.POST['category']
            category = Category.objects.get(category_name=category_field)
            furniture.category = category
            furniture.save()
            if 'complete' in request.POST:
                return redirect('thanks')
            else:
                return redirect('inventory')
            
        else:
            print(furniture_form.errors)
    else:
        furniture_form = FurnitureForm()
        
    furniture_types = [furniture[0] for furniture in Furniture.FURNITURE_CHOICES]
    return render(request, 'add_inventory.html', {'form':furniture_form, 'furniture':furniture_types})


class ThankYouView(TemplateView):
    template_name = 'thankyou.html'