from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATE_CHOICES = (
('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'),

('Andhra Pradesh','Andhra Pradesh'),
('Arunachal Pradesh','Arunachal Pradesh'),
('Assam','Assam'),
('Bihar', 'Bihar'),
('Chandigarh', 'Chandigarh'),
('Chattisgarh','Chattisgarh'),
('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'),
('Daman and Diu', 'Daman and Diu'),
('Delhi', 'Delhi'),
('Goa', 'Goa'),
('Gujrat', 'Gujrat'),
('Haryana', 'Haryana'),
('Himachal Pradesh', 'Himachal Pradesh'),
('Jammu & Kashmir', 'Jammu & Kashmir'),
('Jharkhand', 'Jharkhand'),
('Karnataka', 'Karnataka'),
('Kerala', 'Kerala'),
('Lakshadweep', 'Lakshadweep'),
('Madhya Pradesh', 'Madhya Pradesh'),
('Maharashtra', 'Maharashtra'),
('Manipur', 'Manipur'),
('Meghalaya', 'Meghalaya'),
('Mizoram', 'Mizoram'),
('Nagaland', 'Nagaland'),
('Odisa', 'Odisa'),
('Puducherry', 'Puducherry'),
('Punjab', 'Punjab'),
('Rajasthan', 'Rajasthan'),
('Sikkim', 'Sikkim'),
('Tamil Nadu', 'Tamil Nadu'),
('Telangana', 'Telangana'),
('Tripura', 'Tripura'),
('Uttarakhand', 'Uttarakhand'),
('Uttar Pradesh', 'Uttar Pradesh'),
('West Bengal', 'West Bengal'),
)

CATEGORY_CHOICES=(
    ('CR','Curd'),
    ('ML','Milk'),
    ('LS','Lassi'),
    ('MS','Milkshake'),
    ('PN','Panner'),
    ('GH','Ghee'),
    ('CZ','Cheeze'),
    ('IC','Ice-Creams'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title
    
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)    
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=100)
    
    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)    
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

STATUS_CHOICES=(
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
    ('Pending', 'Pending'),
)

class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True) 
    razorpay_payment_status = models.CharField(max_length=100, blank=True, null=True) 
    razorpay_payment_id= models. CharField(max_length=100, blank=True, null=True) 
    paid = models.BooleanField(default=False)        

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE) 
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models. PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")
    payment = models. ForeignKey(Payment,on_delete=models.CASCADE, default="") 
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price        
