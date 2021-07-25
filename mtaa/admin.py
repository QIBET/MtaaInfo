from django.contrib import admin

# Register your models here.

from .models import Profile,Post,Business,Neighbourhood

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Neighbourhood)