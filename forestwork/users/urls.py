from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='users'),
    path('employers/', views.EmployerListView.as_view(), name='employers'),
    path('employers/<int:user_id>', views.employer, name='employer'),
    path('developers/', views.developers, name='developers'),
    path('developers/<int:user_id>', views.developer, name='developer'),
    path('profile', views.profile, name='profile'),
    path('profile/jobs', views.profile_jobs, name='profile_jobs'),
    path('profile/main', views.profile_main, name='profile_main'),
    path('profile/contacts', views.profile_contacts, name='profile_contacts'),
    path('profile/password', views.profile_password, name='profile_password'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout_view, name='logout')
]