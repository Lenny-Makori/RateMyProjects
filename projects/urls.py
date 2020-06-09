from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('', views.index, name = "homepage"),
    path('profile/<user_id>', views.profile, name='profileview'),
    path('project/<project_id>',views.project,name ='projectview'),
    path('profile/edit/<user_id>', views.update_profile, name = 'profileedit'),
    path('new/project', views.new_project, name='new_project'),
    path('review/<project_id>', views.review_project, name='review'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)