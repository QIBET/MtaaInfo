from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('register/', views.register, name="register"),
	path('login/', views.loginUser, name="login"), 
    path('logout/',views.logoutUser,name="logout") ,
    path(r'^profile/$', views.profile,name='profile'),
    path(r'^edit/$',views.profile_update,name='edit'),
]