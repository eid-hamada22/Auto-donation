from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.

study_supplies = [
    ('stationery','stationery'),
    ('g1','g1'),('g2','g2'),('g3','g3'),
    ('g4','g4'),('g5','g5'),('g6','g6'),
    ('g7','g7'),('g8','g8'),('g9','g9'),
    ('g10','g10'),('g11_sen','g11_sen'),
    ('g11_lit','g11_lit'),('g12_sen','g12_sen')
    ,('g12_lit','g12_lit')
]
clothes = [
    ('babys','babys'),('child','child'),
    ('girls','girls'),('boys','boys'),
    ('men','men'),('womon','womon')
]

class delivery_point(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30,choices=[('mosque','mosque'),('Charity','Charity'),('other','other')])
    Lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=100,null=True,blank=True)
    entry_date = models.DateTimeField(auto_now_add=True)
    user =  models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    user_phone_num = PhoneNumberField(unique=True,null=True)

    def __str__(self):
        return self.name

class item(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='items/')
    entry_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class item_desire(models.Model):
    item_c = models.ForeignKey('item',on_delete=models.CASCADE)
    beneficiary_c = models.ForeignKey('beneficiary',on_delete=models.CASCADE)
    desire_scale = models.IntegerField(choices=[(0,0),(6,6),(7,7),(8,8),(9,9),(10,10)])
    entry_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.entry_date)
    
class item_demand(models.Model):
    delivery_point_c = models.ForeignKey(delivery_point,on_delete=models.CASCADE)
    bio = models.CharField(max_length=150)
    entry_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bio
    
    
class donation(models.Model):
    delivery_point_c = models.ForeignKey(delivery_point,on_delete=models.SET_NULL,null=True)
    item_c = models.ForeignKey(item,on_delete=models.SET_NULL,null=True,blank=True)
    pieces_number = models.IntegerField()
    bio = models.CharField(max_length=120)
    type = models.CharField(max_length=30,choices=[('clothes','clothes'),('study_supplies','study_supplies')])
    study_supplies_type = models.CharField(max_length=30,blank=True,null=True,choices=study_supplies)
    clothes_type = models.CharField(max_length=30,blank=True,null=True,choices=clothes)
    img = models.ImageField(upload_to='donation/')
    recipient = models.BooleanField(default=False)
    notes = models.CharField(max_length=30,blank=True,null=True)
    entry_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.type

class message(models.Model):
    receipt_c = models.ForeignKey('receipt',on_delete=models.SET_NULL,null=True)
    done = models.BooleanField(default=False)
    entry_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.receipt_c)

class receipt(models.Model):
    beneficiary = models.ForeignKey('beneficiary',on_delete=models.SET_NULL,null=True)
    donation = models.ForeignKey(donation,on_delete=models.SET_NULL,null=True)
    message_c = models.ForeignKey(message,on_delete=models.SET_NULL,null=True)
    entry_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.entry_date)

class registrar(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30,choices=[('Charity','Charity'),('Governmental_institution','Governmental_institution'),('other','other')])
    entry_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name

class beneficiary(models.Model):
    name = models.CharField(max_length=30)
    phone_num = PhoneNumberField(unique=True)
    id_ps = models.IntegerField()
    Lat = models.DecimalField(max_digits=9, decimal_places=6)
    long = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=100,null=True,blank=True)
    registrar = models.ForeignKey(registrar,on_delete=models.SET_NULL,null=True)
    need_scale = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)])
    clothes_accept = models.BooleanField(default=False)
    study_supplies_accept = models.BooleanField(default=False)
    study_supplies_needed_type = models.CharField(max_length=30,blank=True,null=True,choices=study_supplies)
    clothes_needed_type = models.CharField(max_length=30,blank=True,null=True,choices=clothes)
    entry_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class user_message(models.Model):
    name = models.CharField(max_length=30)
    phone_num = models.CharField(max_length=30,null=True,blank=True)
    email = models.EmailField(max_length=30)
    message = models.CharField(max_length=255)
    readed = models.BooleanField(default=False)
    entry_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name