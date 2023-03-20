from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile'),
    path('jobs', views.ProfileJobListView.as_view(), name='profile_jobs'),
    path('main', views.ProfileMainUpdateView.as_view(), name='profile_main'),
    path('contacts', views.ProfileContactsUpdateView.as_view(), name='profile_contacts'),
    path('password', views.ProfilePasswordUpdateView.as_view(), name='profile_password'),
    path('messages', views.ProfileMessageListView.as_view(), name='profile_messages'),
    path('messages/<int:pk>', views.ProfileMessageDetailView.as_view(), name='profile_message'),

]