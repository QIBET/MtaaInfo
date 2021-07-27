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
       
        self.bernard.save_profile()
        all_profiles = Profile.get_profile()
        self.assertTrue(len(all_profiles) < 1)
class NeighbourhoodTestCase(TestCase):
    def setUp(self):
        self.new_neighborhood= Neighbourhood(hood_name ='Kadeya',location = 'Nairobi',image = 'kadeya.jpg',description = 'lavish stand-alone villas',user = 'bernard', health_contact= '00100',police_contact= '999',occupant_count ='1')


    def test_save_neighbourhood(self):
        self.new_neighborhood.save_hood()
        hoods = Neighbourhood.objects.all()
        self.assertEqual(len(hoods)>0)

    def test_delete_image(self):
        self.new_neighborhood.save_hood()
        self.new_neighborhood.delete_hood()
        hoods = Neighbourhood.objects.all()
        self.assertTrue(len(hoods)==0)

    def test_get_hoods(self):
       
        self.new_neighborhood.save_hood()
        hoods = Neighbourhood.get_neighbourhood()
        self.assertTrue(len(hoods) < 1)
