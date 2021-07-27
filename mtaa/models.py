import cloudinary
from cloudinary.models import CloudinaryField
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    '''
    class to create instances of profiles
    '''
    image=CloudinaryField('image',blank=True,null=True)
    bio=models.TextField(max_length=100)
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile',primary_key=True)
    email=models.EmailField(max_length=254, blank=True,null=True)
    contact=models.CharField(max_length=40,null=True)
    neighbourhood = models.ForeignKey("Neighbourhood",on_delete=models.CASCADE, default='', null=True, blank=True)

    def _str_(self):
        return self.bio

    def save_profile(self):
        self.save() 

    def delete_profile(self):
        self.delete() 
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):

        if created:
            Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
        
    @classmethod 
    def get_profile(cls):
       profile=Profile.objects.all()
       return profile 

    @classmethod
    def search_profile(cls,search_term):
        hoods = cls.objects.filter(user__icontains=search_term)
        return hoods

class Neighbourhood(models.Model):
    hood_name = models.CharField(max_length=50)
    image = CloudinaryField('image',null=True, blank=True)
    location = models.CharField(max_length=50)
    admin = models.ForeignKey("Profile",on_delete=models.CASCADE, related_name = 'hood',null=True) 
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
    def get_neighbourhood(cls):
        all_hoods=cls.objects.all()
        return all_hoods
    @classmethod
    def search_hood(cls,search_term):
        hoods = cls.objects.filter(hood_name__icontains=search_term)
        return hoods
    @classmethod
    def find_neighbourhood(cls, neighbourhood_id):
        return cls.objects.filter(id=neighbourhood_id)

class Business(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    description = models.TextField(blank=True)
    hood_name = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE,default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return f'{self.name}Business'

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def neighbourhood_business(cls, id):
        allhood_business = Business.objects.filter(hood_name = id)
        return allhood_business

class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hood_name= models.ForeignKey(Neighbourhood, on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return f'{self.title} Post'
    
    @classmethod
    def hood_post(cls,id):
        hoodposts = Post.objects.filter(hood_name = id)
        return hoodposts

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()