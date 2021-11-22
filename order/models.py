from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Value
from user.models import Account
from django.urls import reverse


class Category(models.Model):
    CATEGORY_CHOICES = [('Living Room','Living Room'),
    ('Bedroom', 'Bedroom'), ('Dining Room', 'Dining Room'),
    ('Home Office','Home Office'), ('Bedding', 'Bedding'),
    ('Accents', 'Accents')]

    category_name = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    def __str__(self) -> str:
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Address(models.Model):
    street_address = models.CharField(max_length=100,blank=True )
    city = models.CharField(max_length=100, blank= True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.street_address)+ ', ' + str(self.city) + ', '+ str(self.state) + ', '+str(self.zip_code)

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    address = models.ForeignKey(Address, blank=True, null=True, on_delete=CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_url(self):
        return reverse('furniture_by_customer', args=[self.pk])

class Furniture(models.Model):
    COLOR_CHOICES = [
    ('Black', 'Black'),
    ('Blue', 'Blue'),
    ('Brown', 'Brown'),
    ('Burgandy', 'Burgandy'),
    ('Grey', 'Grey'),
    ('White', 'White'),
    ('Tan', 'Tan'),
    ('Other', 'Other')]

    FINISH_CHOICES = [('Ebony','Ebony'),
    ('Mahogany', 'Mahogany'),
    ('Cherry', 'Cherry'),
    ('Oak', 'Oak'),
    ('Espresso', 'Espresso'),
    ('Other', 'Other')]

    UPHOLSTERY_CHOICES = [('Fabric', 'Fabric'),
    ('Leather', 'Leather')]

    STATUS_CHOICES = [('Waiting','Waiting'),
                    ('Pending','Pending'),
                    ('Complete', 'Complete')]
                
    CONDITION_CHOICES = [('New','New'),
                ('Used', 'Used'),
                ('Good', 'Good'),
                ('Damaged','Damaged')]


    LOCATION_CHOICES = [('Lodi','Lodi')]

    UNIT_CHOICES=[('1085','1085'),('1086','1086'), ('1087','1087'),('1088','1088'), ('1039','1039'),('1038','1038')]

    SOURCE_CHOICES=[('Raymour & Flanigan', 'Raymour & Flanigan'), ('Facebook', 'Facebook')]

    FURNITURE_CHOICES = [('Sofa & Loveseat', 'Sofa & Loveseat'),
                     ('Sectionals', 'Sectionals'),
                     ('Sofa', 'Sofa',),
                     ('Loveseat','Loveseat'),
                     ('Recliner', 'Recliner'),
                     ('Chair', 'Chair' ),
                     ('Coffee Table', 'Coffee Table'),
                     ('End Table', 'End Table'),
                     ('Ottoman', 'Ottoman'),
                     ('TV Console', 'TV Console'),
                     ('Fireplaces', 'Fireplaces'),
                     ('Office Desks', 'Office Desks'),
                     ('Office Chairs', 'Office Chairs'),
                     ('Bookcases', 'Bookcases'),
                     ('File Cabinets', 'File Cabinets'),
                     ('Twin Bed', 'Twin Bed'),
                     ('Queen Bed', 'Queen Bed'),
                     ('King Bed', 'King Bed'),
                     ('Dresser', 'Dresser'),
                     ('Nightstand', 'Nightstand'),
                     ('Chest', 'Chest'),
                     ('Twin Mattress', 'Twin Mattress'),
                     ('Full Mattress', 'Full Mattress'),
                     ('Queen Mattress', 'Queen Mattress'),
                     ('King Mattress', 'King Mattress'),
                     ('Adjustable Base', 'Adjustable Base'),
                     ('Box Spring', 'Box Spring'),
                     ('Counter Height Set', 'Counter Height Set'),
                     ('Dining Set', 'Dining Set'),
                     ('Table', 'Table'),
                     ('Dining Chairs', 'Dining Chairs'),
                     ('Bar Height Stools', 'Bar height Stools'),
                     ('Counter Height Stools', 'Counter Height Stools'),
                     ('Island', 'Island'),
                     ('China/Buffet', 'China/Buffet')]    


    category  = models.ForeignKey(Category, on_delete=CASCADE, blank=True, null=True)
    sub_category = models.CharField(choices = FURNITURE_CHOICES, max_length=1000, null = True, blank = True)
    sku = models.CharField(max_length=100, null = True, blank=True, unique=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    condition = models.CharField(choices=CONDITION_CHOICES, max_length=100, blank=True)
    color = models.CharField(choices=COLOR_CHOICES, max_length=100, blank=True)
    finish = models.CharField(choices=FINISH_CHOICES, max_length=100, blank=True)
    upholstery= models.CharField(choices=UPHOLSTERY_CHOICES, max_length=100, blank=True)
    pcs = models.IntegerField(default=1, null=True, blank=True)
    cost = models.IntegerField(null=True,blank=True)
    list_price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(default=1, blank=True, null=True)
    source = models.CharField(blank=True, null=True, max_length=100, choices=SOURCE_CHOICES)
    location = models.CharField(choices=LOCATION_CHOICES, max_length=100, null=True, default='Lodi', blank=True)
    unit_number = models.IntegerField(null=True, blank=True)
    listed = models.BooleanField(null=True, default=False, blank=True)
    picture = models.ImageField(null=True, blank=True)
    comments = models.TextField(max_length=2000, null = True, blank=True)

    def __str__(self):
        return str(self.sku)+' '+'-'+ ' '+str(self.name)
    
    class Meta:
        verbose_name = 'Furniture'
        verbose_name_plural = 'Furniture'
    

class Ticket(models.Model):
    ticket_id = models.CharField(max_length=200, blank=True)
    customer = models.ForeignKey(Customer, on_delete=CASCADE, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id) 
    
    @property
    def get_ticket_total(self):
        ticketitems = self.ticketitem_set.all()
        return sum([item.get_total for item in ticketitems])
    
    @property
    def get_ticket_profit(self):
        ticketitems = self.ticketitem_set.all()
        return sum([item.get_total for item in ticketitems])- sum([item.get_cost for item in ticketitems])


class TicketItem(models.Model):
    furniture = models.ForeignKey(Furniture, on_delete=models.SET_NULL, null=True)
    ticket = models.ForeignKey(Ticket, on_delete=models.SET_NULL, null=True) 
    price = models.FloatField(default=0.00)
    quantity = models.IntegerField(default=1, null =True, blank=True)
    
    @property
    def get_total(self):
        return self.price * self.quantity

    @property
    def get_cost(self):
        return self.furniture.cost * self.furniture.quantity

    class Meta:
        verbose_name = 'Ticket Item'
        verbose_name_plural = 'Ticket Items'