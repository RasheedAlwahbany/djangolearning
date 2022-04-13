from pickle import TRUE
from django.db import models

# Create your models here.

class Accounts(models.Model):
    Id=models.AutoField(primary_key=True)
    uname=models.CharField(max_length=40)
    #this is when the posts depends on account and the opesite we do this to prevent loop dependency
    featured_posts=models.ForeignKey('Posts',blank=True, on_delete=models.SET_NULL, null=True,related_name='+')
    
    def __str__(self) -> str:
        return self.uname
    class Meta:
        db_table='Accounts'
        indexes=[models.Index(fields=['uname'])]
        
    
class Posts(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    #this is one to many relationship
    account_id=models.ForeignKey(Accounts,on_delete=models.CASCADE) 
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table='Posts'
    
    
class Phones (models.Model):
    Id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    #this is a many to many relationship
    account=models.ManyToManyField(Accounts) 

    def __str__(self) -> str:
        return self.name    
    class Meta:
        db_table='Phones'
    
class Address(models.Model):
    street=models.CharField(max_length=40)
    city=models.CharField(max_length=40)
    state=models.CharField(max_length=40)
    zip=models.CharField(max_length=40)
    #this is one to one relationship
    account_id=models.OneToOneField(Accounts,on_delete=models.CASCADE,primary_key=True) 
    
    def __str__(self) -> str:
        return self.city
    class Meta:
        db_table='Address'
    
    


