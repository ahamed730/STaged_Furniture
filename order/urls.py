from django.urls import path
from . import views



urlpatterns = [
    path('add-furniture/', views.furnitureform, name = 'inventory'),
    path('thanks/', views.ThankYouView.as_view(), name = 'thanks')
    
]