from django.test import TestCase
from .models import Profile,Neighbourhood, Business,Post
from django.contrib.auth.models import User
# Create your tests here.

class ProfileTestCase(TestCase):
    def setUp(self):
        self.bernard = User(username = 'bernard',email = 'bennykibet@gmail.com')
        self.bernard = Profile(user = self.bernard,user_id = 1,bio = 'Focus and Integrity', email='test@gmail.com',contact = '0724835573',image = 'benny.jpg', neighbourhood='Kadeya')

    def test_instance(self):
        self.assertTrue(isinstance(self.bernard,Profile))

    def test_save_profile(self):
        self.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    
    def test_delete_profile(self):
        self.bernard.save_profile()
        self.bernard.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)
    
    def test_get_all_profiles(self):
       
        self.profiles.save_profile()
        all_profiles = Profile.get_profile()
        self.assertTrue(len(all_profiles) < 1)

