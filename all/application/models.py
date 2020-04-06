from django.db import models
from django.core import validators
from django.db import models
from django.db import models
from django.utils import timezone
from django.conf import settings






# Create your models here.
COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)

GENDER_CHOICES = (
    
    ('Male', 'Male'),
    ('Female','Female'),

)


#class FrontPagination(models.Model):



class Post2(models.Model):
	title = models.CharField(max_length = 100)
	content = models.TextField()
	publish = models.DateField(auto_now=True, auto_now_add = False)    







class City(models.Model):
    city_name = models.CharField(max_length=30,help_text='Enter City Name')
    city_code = models.CharField(max_length=4)
    class Meta:
        ordering = ['city_name']

    def __str__(self):
        return self.city_name
     
class State(models.Model):
    state_name =models.CharField(max_length=20)
    state_code =models.CharField(max_length=4)
    city = models.ManyToManyField(City)
    class Meta:
        ordering = ['state_name']
    def __str__(self):
        return self.state_name







# Relationship Demo
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, null=True) #    If True, Django will store empty values as NULL in the database. Default is False.
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    def __str__(self):
        return self.name
 
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    def __str__(self):
        return self.first_name +' '+self.last_name
 
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
    publication_date = models.DateField()
    def __str__(self):
        return self.title

#  End Relationship






class UserRegistration(models.Model):
    username = models.CharField(max_length=20)
    useremail = models.EmailField(max_length=29)
    userpass = models.CharField(max_length=20)
    





class Person(models.Model):
    per_name = models.CharField(max_length=24)
    father_name =models.CharField(max_length=200)
    gender =models.CharField(max_length=22,choices=GENDER_CHOICES,default='Male')
    mobile = models.CharField(max_length=10)
    per_address =models.TextField(max_length=555,default=None)
    per_pincode = models.CharField(max_length=6,default=None)
    per_photo   = models.FileField(upload_to='images/',default=None)
    per_status = models.BooleanField('Are You Married',default=True)

    def __str__(self):
        return self.per_name


class Student(models.Model):
    stu_name = models.CharField(max_length=255, default=None)
    father_name = models.CharField(max_length=255,default=None)
    dob = models.DateField()
    stu_gender =models.CharField(max_length=20,choices=GENDER_CHOICES,default='Male')
    stu_mobile =models.CharField(max_length=11,default=None)
    stu_address =models.TextField(max_length=555,default=None)
    stu_pincode = models.CharField(max_length=6,default=None)
    stu_photo   = models.ImageField(upload_to='images/',default=None)
    stu_status = models.BooleanField('Are You Married',default=False)
    
    def admin_thumbnail(self):
        return u'<img src="%s" />' % (self.stu_photo.url)
        admin_thumbnail.allow_tags = True

    def __str__(self):
        return self.stu_name
    








# oneToone Relationship Demo
class Category(models.Model):
    category = models.CharField(max_length=30)   
    def __str__(self):
        return self.category 

class Post(models.Model):
    title = models.CharField(max_length=24)
    description = models.TextField(max_length=255)
    def __str__(self):
        return self.title

    




class Organization(models.Model):
    orgName = models.CharField(max_length=22)
    orgEmail = models.EmailField(max_length=25)
    orgContact = models.IntegerField(max_length=10)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now_add=True)

class Company(models.Model):
    comp_name = models.CharField(max_length=50)
    comp_email = models.EmailField(max_length=254)
    comp_code = models.CharField(max_length=254)
    comp_mobile = models.CharField(max_length=10)
    comp_address = models.TextField(max_length=254)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now_add=True)