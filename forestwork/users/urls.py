from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='users'),
    path('employers/', views.EmployerListView.as_view(), name='employers'),
    path('employers/<int:pk>', views.EmployerDetailView.as_view(), name='employer'),
    path('developers/', views.DeveloperListView.as_view(), name='developers'),
    path('developers/<int:pk>', views.DeveloperDetailView.as_view(), name='developer'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('profile/jobs', views.ProfileJobListView.as_view(), name='profile_jobs'),
    path('profile/main', views.ProfileMainUpdateView.as_view(), name='profile_main'),
    path('profile/contacts', views.ProfileContactsUpdateView.as_view(), name='profile_contacts'),
    path('profile/password', views.profile_password, name='profile_password'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name='logout')
]