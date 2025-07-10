from django.db import models
from  decimal import Decimal


class  BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class  Category(BaseModel):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['title']
        verbose_name = 'Category'
    

# Create your models here.
class Product(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    discount = models.IntegerField(default=0)
    category  =  models.ForeignKey(Category, related_name='products', on_delete= models.SET_NULL, null=True  , blank=True)

    @property
    def  discounted_price(self):
        if self.discount > 0:
            return self.price * Decimal(f"{ 1- (self.discount / 100)}")
        return self.price

    def  __str__(self):
        return  f"{  self.name}  {self.price}"

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ['-id']
        verbose_name = 'Product'
        ordering = ['price']


class  Order(BaseModel):
    user = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return f"Order {self.id} by {self.user}"

    class Meta:
        verbose_name_plural = 'Orders'
        verbose_name = 'Order'