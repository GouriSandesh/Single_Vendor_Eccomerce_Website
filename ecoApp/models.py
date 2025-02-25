import random

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils import timezone


class User(AbstractUser):
    is_customer = models.BooleanField(default=False)

gender = [
    ['Male','Male'],
    ['Female', 'Female'],
    ['Not To Disclose','Not To Disclose']
]
class Customers(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True,related_name='cust')
    Name=models.CharField(max_length=255)
    Mobile=models.CharField(max_length=10)
    pro_pic = models.ImageField(upload_to='userPics')
    Email=models.EmailField()
    Gender=models.CharField(max_length=255,choices=gender,default='none')


    def __str__(self):
        return self.Name

states=(
    ('Andhra Pradesh','Andhra Pradesh'),
    ('Arunachal Pradesh ', 'Arunachal Pradesh '),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Goa', 'Goa'),
    ('Gujarat', 'Gujarat'),
    ('Haryana', 'Haryana'),
    ('Himachal Pradesh', 'Himachal Pradesh'),
    ('Jammu & Kashmir', 'Jammu & Kashmir'),
    ('Jharkhand', 'Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Ladakh','Ladakh'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya','Meghalaya'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
    ('Odisha', 'Odisha'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim', 'Sikkim'),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Telangana', 'Telangana'),
    ('Tripura', 'Tripura'),
    ('Uttarakhand','Uttarakhand'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('West Bengal','West Bengal'),
)

type=[
    ['Home','Home'],
    ['Office','Office'],
    ['Other','Other']
]
class addressBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Address_line1 = models.CharField(max_length=255)
    Address_line2 = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    District= models.CharField(max_length=255)
    state = models.CharField(max_length=100,choices=states, default='select')
    pin_code = models.CharField(max_length=6)
    address_type = models.CharField(max_length=20,choices=type, default='select')  # E.g., 'Home', 'Office'

    def __str__(self):
        return f"{self.user.username} - {self.city}"


categoryChart=(
    ('Women','Women'),
    ('Men','Men'),
    ('Kids','Kids'),
    ('Bags','Bags'),
    ('Jewellery','Jewellery'),
    ('Footwear','Footwear'),
    ('Shirts','Shirts'),
)

subChart = (
    ('Sarees','Sarees'),
    ('Kurta&Kurtis','Kurta&Kurtis'),
    ('Lehanga','Lehanga'),
    ('Gowns','Gowns'),
    ('Topwear','Topwear'),
    ('T-shirts','T-shirts'),
    ('FShirts','FShirts'),
    ('CShirts','CShirts'),
    ('WJeans','WJeans'),
    ('Jumpsuits','Jumpsuits'),
    ('Jeggings','Jeggings'),
    ('BoysClothing','BoysClothing'),
    ('GirlsClothing','GirlsClothing'),
    ('Leggings','Leggings'),
    ('EthnicSet','EthinicsSet'),
    ('MJeans','MJeans'),
    ('ArtJewel','ArtJewel'),
    ('SilverJewel','SilverJewel'),
    ('Totes','Totes'),
    ('ksuits','ksuits'),
    ('Earrings','Earrings'),
    ('Gold','Gold'),
    ('Necklace','Necklace'),
    ('Anklets','Anklets'),
    ('Rings','Rings'),
    ('Flats','Flats'),
    ('SBags','SBags'),
    ('HandBags','HandBags'),
    ('Clutches','Clutches'),
    ('SShoes','SShoes'),
    ('CShoes','CShoes'),
    ('Chains','Chains'),
    ('trackpant','trackpant'),
    ('Pendant','Pendant'),
    ('Wallet','Wallet'),
    ('Watch','Watch'),
    ('Heels','Heels'),
    ('Boots','Boots'),
    ('SlBags','SlBags'),
    ('TBags','TBags'),
    ('Sherwanis','Sherwanis'),
    ('Blazzers','Blazzers'),
    ('Gfrocks','Gfrocks'),
    ('Gdung','Gdung'),
    ('Bshirts','Bshirts'),
    ('Gtops','Gtops'),
    ('KTshirts','KTshirts'),
    ('Jackets','Jackets'),
    ('Bangles','Bangles'),
    ('Hobo','Hobo'),
    ('Crossbody','Crossbody'),
    ('Messanger','Messanger'),
    ('backpack','backpack'),
)

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='pdtImages')
    image2 = models.ImageField(upload_to='pdtImages')
    image3 = models.ImageField(upload_to='pdtImages')
    brand = models.CharField(max_length=255)
    MRP = models.CharField(max_length=255)
    QTY = models.IntegerField(db_column='numbers', blank=False, default=0)
    price = models.IntegerField()
    Category = models.CharField(max_length=255, choices=categoryChart, default='select')
    Sub_Category = models.CharField(max_length=255, choices=subChart, default='select')

    def _str_(self):
        return f"{self.product_name} |  {self.image} | {self.QTY} | {self.price}"




class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Wishlist of {self.user.username}"


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.product.product_name} in wishlist of {self.wishlist.user.username}"


class CartManager(models.Manager):
    def get_cart_for_user(self, user):
        return self.get(user=user)



class Cart(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return f"Cart of {self.user.username}"




class CartItem(models.Model):
   cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   quantity = models.PositiveIntegerField(default=1)
   unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


   def __str__(self):
       return f"{self.quantity} x {self.product.product_name} of {self.product.price}"



class Order(models.Model):
        order_id = models.CharField(max_length=13, unique=True, editable=False)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        order_date = models.DateTimeField(auto_now_add=True)
        total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


        def save(self, *args, **kwargs):
            if not self.order_id:
                # Generate a random 13-digit order ID if it doesn't already exist
                self.order_id = str(random.randint(1000000000000, 9999999999999))
            super().save(*args, **kwargs)

        def __str__(self):
            return f"Order {self.order_id} by {self.user.username} "



class OrderItem(models.Model):
        order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
        product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
        quantity = models.PositiveIntegerField()
        unit_price = models.DecimalField(max_digits=10, decimal_places=2)
        total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

        def save(self, *args, **kwargs):
            # Calculate total price for this item based on quantity and unit price
            self.total_price = self.quantity * self.unit_price
            super().save(*args, **kwargs)

        def __str__(self):
            return f"{self.quantity} x {self.product.product_name}"



payment_method = [
    ('card', 'Credit/Debit Card'),
    ('upi', 'UPI'),
    ('bank_transfer', 'Bank Transfer'),
    ('cod', 'Cash On Delivery')
]

payment_status = [
    ('P', 'Pending'),
    ('S', 'Shipped'),
    ('D', 'Delivered'),
    ('C', 'Cancelled'),
]

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    payment_method = models.CharField(max_length=20, choices=payment_method)  # Use a list here
    transaction_id = models.CharField(max_length=100, unique=True, blank=True, null=True)
    payment_date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=1, choices=payment_status, default='P')
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Payment {self.transaction_id or 'N/A'} - {self.get_status_display()} by {self.user.username}"

    class Meta:
        ordering = ['-payment_date']


class CustomerTraffic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    path = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    duration = models.FloatField()  # Time spent on page in seconds

    def __str__(self):
        return f"{self.user} visited {self.path} at {self.timestamp}"


