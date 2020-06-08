from django.shortcuts import render

# Create your views here.

def index(request):
    test = "Nakucheki nakudigi"

    return render(request, 'mainview/mainpage.html', {"image_display":test})