from django.shortcuts import render

# Create your views here.

def index(request):
    test = "Nakucheki nakudigi"

    return render(request, 'mainview/mainpage.html', {"image_display":test})

def profile(request, user_id):
    user_profile = Profile.get_profile(user_id)

    return render(request, 'profile.html', {'user_profile':user_profile})