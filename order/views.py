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
    categories = [category[0] for category in Category.CATEGORY_CHOICES]    
    furniture_types = [furniture[0] for furniture in Furniture.FURNITURE_CHOICES]
    colors = [color[0] for color in Furniture.COLOR_CHOICES]
    finishes = [finish[0] for finish in Furniture.FINISH_CHOICES]
    upholstery = [upholstery[0] for upholstery in Furniture.UPHOLSTERY_CHOICES]
    condition = [condition[0] for condition in Furniture.CONDITION_CHOICES]
    quantity = [num for num in range(100)]
    pcs = [num for num in range(100)]
    sources = [source[0] for source in Furniture.SOURCE_CHOICES]
    locations = [location[0] for location in Furniture.LOCATION_CHOICES]
    units = [unit[0] for unit in Furniture.UNIT_CHOICES]

    return render(request, 'add_inventory.html', {'form':furniture_form, 
    'furniture':furniture_types, 'categories':categories, 
    'colors':colors,'upholstery':upholstery, 
    'condition':condition,'finishes':finishes,
    'quantity':quantity, 'pcs':pcs,
    'sources':sources, 'locations':locations,
    'units':units})


class ThankYouView(TemplateView):
    template_name = 'thankyou.html'