from django.shortcuts import render, redirect, get_object_or_404
from .models import Project, Profile
from .forms import ProfileForm, ProjectForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    test = "Nakucheki nakudigi"

    return render(request, 'mainview/mainpage.html', {"image_display":test})

@login_required(login_url='/accounts/login/')
def profile(request, user_id):
    user_profile = Profile.get_profile(user_id)

    return render(request, 'profile.html', {'user_profile':user_profile})

@login_required(login_url='/accounts/login/')
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


@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = current_user
            project.save()
        return redirect('homepage')
    else:
        form = ProjectForm()
    return render(request, 'new_project.html', {'form': form})


def review_project(request, project_id):
    image = get_object_or_404(Project, id=project_id)
    current_user = request.user
    if request.method == 'POST':
            reviewform = ProjectForm(request.POST, request.FILES)
            if reviewform.is_valid:
                review = reviewform.save(commit=False)
                review.user = current_user
                review.project = project
                review.save()
            return redirect('projectview')
    else:
        commentform = ProjectForm()
    return render(request, 'project_review.html', {"form": reviewform})