from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render,get_object_or_404
from .models import Profile,Neighbourhood,Business,Post
from .forms import ProfileForm,NeighbourhoodForm,BusinessForm,PostForm

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
            hood.save()
            return redirect('index')
    else:
        form = NeighbourhoodForm()
    return render(request,'newneighbourhood.html', {"form":form})



def businesses(request, id):
    business = Business. neighbourhood_biz(id=id)
    return render(request, 'business.html', {'business': business})

def singlehood(request, id):
    hood = Neighbourhood.objects.get(id=id)
    return render(request, 'single_hood.html', {'hood':hood})

def newBusiness(request):
    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user

            business.save()

        return redirect('index')

    else:
        form = BusinessForm()
    return render(request, 'newbusiness.html', {"form": form})
def joinhood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = hood
    request.user.profile.save()
    return redirect('index')


def leavehood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('index')

def post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user

            post.save()

        return redirect('index')

    else:
        form = PostForm()
    return render(request, 'new_post.html', {"form": form})

def neighbourhood_post(request, id):
    posts = Post.hood_post(id=id)
    return render(request, 'post.html', {'posts': posts})