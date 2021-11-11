from django.contrib import admin
from order.models import Category, Furniture, Address, Customer,Ticket, TicketItem

admin.site.register(Furniture)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Ticket)
admin.site.register(TicketItem)