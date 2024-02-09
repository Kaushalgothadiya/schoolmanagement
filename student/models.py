from django.db import models
from django.contrib.auth.models import User




# many to many relationship:
class Course(models.Model):
    name=models.CharField(max_length=50)
    students=models.ManyToManyField('Student',related_name='courses')

    def __str__(self) -> str:
        return self.name
    

# Create your models here.
class Section(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class Student(models.Model):
    name=models.CharField(max_length=50)
    section=models.ForeignKey(Section,related_name='students',on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self) -> str:
        return self.name

    @property
    def price_including_tax(self):
        tax_price=0.10
        return self.price*(1+0.10)
    
    @property
    def is_expensive(self):
        expensive_threshold=100
        return self.price>expensive_threshold
    

class Items(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    price_including_tax=models.DecimalField(max_digits=20,decimal_places=2,null=True,blank=True,editable=False)

    def save(self,*args,**kwargs):
        if self.price is not None and self.price_including_tax is None:
            self.price_including_tax=self.price*self.price
        super().save(*args,**kwargs)

    def __str__(self) -> str:
        return self.name

    # @property
    # def price_including_tax(self):
    #     tax_price='0.10'
    #     return float(self.price*(1+tax_price))

    
            