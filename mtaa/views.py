from django.shortcuts import render

# Create your views here.

def index(request):
    title = "MtaaInfo Application"

    return render(request, 'index.html',{"title":title})
