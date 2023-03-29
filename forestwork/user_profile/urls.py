from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile'),
    path('jobs', views.ProfileJobListView.as_view(), name='profile_jobs'),
    path('main', views.ProfileMainUpdateView.as_view(), name='profile_main'),
    path('contacts', views.ProfileContactsUpdateView.as_view(), name='profile_contacts'),
    path('specializations', views.ProfileSpecializationUpdateView.as_view(), name='profile_specializations'),
    path('password', views.ProfilePasswordUpdateView.as_view(), name='profile_password'),
    path('chats', views.ProfileChatListView.as_view(), name='profile_chats'),
    path('chat/<int:pk>', views.ProfileChatDetailView.as_view(), name='profile_chat'),
    path('chat/delete/<int:pk>', views.ProfileChatDeleteView.as_view(), name='profile_chat_delete'),
]