from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('register/', views.register, name="register"),
	path('login/', views.loginUser, name="login"), 
    path('logout/',views.logoutUser,name="logout") ,
    path('profile/', views.profile,name='profile'),
    path('edit/',views.profile_update,name='edit'),
    path('neighbourhood/', views.create_neighbourhood,name='newneighbourhood'),
    path('businesses/<id>', views.businesses, name='hoodbusiness'),
    path('singlehood/<id>', views.singlehood, name='singlehood'),
    path('new_business/', views.newBusiness, name='newbusiness'),
    path('joinhood/<id>', views.joinhood, name='joinhood'),
    path('leavehood/<id>', views.leavehood, name='leavehood'),
    path('post', views.post, name='post'),

]