from django.shortcuts import render
from .models import Project, Profile
from .forms import ProfileForm

# Create your views here.

def index(request):
    test = "Nakucheki nakudigi"

    return render(request, 'mainview/mainpage.html', {"image_display":test})

def profile(request, user_id):
    user_profile = Profile.get_profile(user_id)

    return render(request, 'profile.html', {'user_profile':user_profile})

def update_profile(request, user_id):
    current_user = request.user
    current_user_id = current_user.id
    user_profile = Profile.get_profile(user_id)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()

        return redirect('homepage')
    else:
        form = ProfileForm()

    return render(request, 'profile_edit.html', {"form": form})