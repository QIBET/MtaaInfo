from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from .models import Profile,Neighbourhood
from .forms import ProfileForm,NeighbourhoodForm

from .forms import CreateUserForm

# Create your views here.

def index(request):
    neighbourhoods = Neighbourhood.get_neighbourhood()
    return render(request, 'index.html', {"neighbourhoods":neighbourhoods})

def register(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'registration/register.html', context)

def loginUser(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username or password is incorrect')

		context = {}
		return render(request, 'registration/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

def profile(request):
    '''
	returns user profile from a pool of profiles
	'''
    current_user=request.user
    profile= Profile.objects.filter(user=current_user).first()
     
    
    return render(request,'profile.html',{"profile":profile,"current_user":current_user})
def profile_update(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('profile')

    else:
        form = ProfileForm()
        return render(request,'update_profile.html',{"form":form})

def create_neighbourhood(request):
    '''
    method that creates neighbourhoods
    '''
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            hood = form.save(commit=False)
           # hood.user = request.user.profile
            hood.save()
            return redirect('index')
    else:
        form = NeighbourhoodForm()
    return render(request,'newneighbourhood.html', {"form":form})
