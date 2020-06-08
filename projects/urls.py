from django.urls import path
from . import views


urlpatterns=[
    path('', views.index, name = "homepage"),
    path('profile/<user_id>', views.profile, name='profileview'),
    path('profile/edit/<user_id>', views.update_profile, name = 'profileedit'),
]