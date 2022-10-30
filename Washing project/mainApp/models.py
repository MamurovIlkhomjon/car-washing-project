from django.db import models
from django.db.models import Q

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, choices = [('admin', 'admin'), ('owner', 'owner'),])
    washcompany = models.ForeignKey('WashCompany', on_delete=models.CASCADE)

    # class Meta:
    #     constraints = (models.UniqueConstraint(
    #         fields=['role','washcompany'], 
    #         name='role and washcompany error', 
    #         condition=models.Q(role='owner')),)

    # def __str__(self):
    #     return self.name


class Car(models.Model):
    car_model = models.CharField(max_length=100)
    car_number = models.CharField(max_length=100)
    owner_name = models.CharField(max_length=100)
    owner_phone = models.CharField(max_length=100)

    # class Meta:
    #     constraints =(models.UniqueConstraint(
    #         fields=['car_model','owner_name','owner_phone'],
    #         name='car_model, car_owner and car_phone error'),)  

    # def __str__(self):
    #     return f'Car model: {self.car_model}, Car number: {self.car_number}'
    

class Washer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    avatar = models.ImageField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class WashCompany(models.Model):
    name = models.CharField(max_length=100)
    avatar = models.ImageField(null=True, blank=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name    
    

class Service(models.Model):
    name = models.CharField(max_length=100)
    time = models.DateTimeField(null=True)
    price = models.PositiveIntegerField()
    washcompany = models.ForeignKey(WashCompany, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    washer = models.ForeignKey(Washer, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    is_active = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now = True, null=True, blank=True)


    def __str__(self):
        return f'Service name:, Washer name:'

    




