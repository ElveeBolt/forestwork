from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='users'),
    path('employers/', views.employers, name='employers'),
    path('employers/<int:user_id>', views.employer, name='employer'),
    path('developers/', views.developers, name='developers'),
    path('developers/<int:user_id>', views.developer, name='developer'),
    path('profile', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]