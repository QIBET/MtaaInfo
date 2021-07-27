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

class BusinessTestCase(TestCase):
    def setUp(self):
        self.new_business= Business(name = 'jerrys',email = 'jerry@gmail',description='Grocery stores',hood_name = 'Kadeya',user = 'Peris',admin='Eric')


    def test_save_business(self):
        self.new_business.save_business()
        businesses = Business.objects.all()
        self.assertEqual(len(businesses)>0)

    def test_delete_business(self):
        self.new_business.save_business()
        self.new_business.delete_business()
        businesses = Neighbourhood.objects.all()
        self.assertTrue(len(businesses)==0)

    def test_get_biz(self):
       
        self.new_business.save_business()
        businesses = Business.neighbourhood_business()
        self.assertTrue(len(businesses) < 1)
class PostTestCase(TestCase):
    def setUp(self):
        self.new_post = Post(title = 'Run',post = 'Great run this morning',date = '26-07-2020',user = 'bernard',hood_name = 'Kadeya')

    def test_save_post(self):
        self.new_post.save_post()
        posts = Post.objects.all()
        self.assertEqual(len(posts)>0)

    def test_delete_post(self):
        self.new_post.save_post()
        self.new_post.delete_post()
        posts = Post.objects.all()
        self.assertTrue(len(posts)==0)

    def test_get_posts_by_id(self):
       
        self.new_post.save_post()
        posts = Post.hood_post()
        self.assertTrue(len(posts) < 1)