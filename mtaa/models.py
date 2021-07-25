import cloudinary
from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    '''
    class to create instances of profiles
    '''
    image=CloudinaryField('image',blank=True,null=True)
    bio=models.TextFields(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.EmailField(max_length=254, blank=True,null=True)
    contact=models.TextField(max_length=40,null=True)

    def _str_(self):
        return self.bio

    def save_profile(self):
        self.save() 

    def delete_profile(self):
        self.delete() 
    @classmethod 
    def get_profile(cls):
       profile=Profile.objects.all()
       return profile 

    @classmethod
    def search_profile(cls,search_term):
        hoods = cls.objects.filter(user__icontains=search_term)
        return hoods

class Neighbourhood(models.Model):
    hood_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    admin = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='hood')
    description = models.TextField()
    health_contact = models.IntegerField(null=True, blank=True)
    police_contact = models.IntegerField(null=True, blank=True)
    occupant_count = models.IntegerField(null=True, blank=True)

    def _str_(self):
        return self.hood_name

    def save_hood(self):
        self.save() 

    def delete_hood(self):
        self.delete() 

    @classmethod
    def search_hood(cls,search_term):
        hoods = cls.objects.filter(hood_name__icontains=search_term)
        return hoods
    @classmethod
    def find_neighbourhood(cls, neighbourhood_id):
        return cls.objects.filter(id=neighbourhood_id)