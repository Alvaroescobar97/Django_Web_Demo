from django.db import models
# Create your models here.
 
class Client(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email =  models.EmailField(max_length = 50) 
 
    def __str__(self):
        return f"id={self.id},name={self.name},phone={self.phone},email={self.email}"
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField() 
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return f"id={self.id},name={self.name},price={self.price},description={self.description}"    
    
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    
    def __str__(self):
        return f"id={self.id}, client={self.client}"