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
    path('profile/password', views.ProfilePasswordUpdateView.as_view(), name='profile_password'),
    path('login', views.UserLoginView.as_view(), name='login'),
    path('login/forgot_password', views.UserForgotPasswordView.as_view(), name='forgot_password'),
    path('login/forgot_password_send', views.UserForgotPasswordSendView.as_view(), name='forgot_password_send'),
    path('login/forgot_password/<uidb64>/<token>', views.UserForgotPasswordVerifyView.as_view(), name='forgot_password_verify'),
    path('login/forgot_password/success', views.UserForgotPasswordVerifySuccessView.as_view(), name='forgot_password_verify_success'),
    path('login/forgot_password/invalid', views.UserForgotPasswordVerifyInvalidView.as_view(), name='forgot_password_verify_invalid'),
    path('register', views.UserRegisterView.as_view(), name='register'),
    path('register/activate', views.UserRegisterActivateView.as_view(), name='register_activate'),
    path('register/verify/<uidb64>/<token>', views.UserRegisterVerifyView.as_view(), name='register_verify'),
    path('register/verify/success', views.UserRegisterVerifySuccessView.as_view(), name='register_verify_success'),
    path('register/verify/invalid', views.UserRegisterVerifyInvalidView.as_view(), name='register_verify_invalid'),
    path('logout', views.UserLogoutView.as_view(), name='logout')
]