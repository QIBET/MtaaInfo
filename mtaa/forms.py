from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db.models import fields
from . models import Neighbourhood, Profile,Business,Post



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
	
    class Meta:
        model = Profile
        exclude = ['user']


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ('hood_name','location','admin','description','health_contact','police_contact','occupant_count','image')

class BusinessForm(forms.ModelForm):
	class Meta:
		model = Business
		exclude = ['neighbourhood','user']

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		exclude = ['hood_name','user']