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
    path('forgot', views.UserForgotView.as_view(), name='forgot'),
    path('forgot/send', views.UserForgotSendView.as_view(), name='forgot_send'),
    path('forgot/verify/<uidb64>/<token>', views.UserForgotVerifyView.as_view(), name='forgot_verify'),
    path('forgot/success', views.UserForgotSuccessView.as_view(), name='forgot_verify_success'),

    path('signup', views.UserSignupView.as_view(), name='signup'),
    path('activate', views.UserActivateView.as_view(), name='signup_activate'),
    path('verify/<uidb64>/<token>', views.UserVerifyView.as_view(), name='signup_verify'),
    path('verify/success', views.UserVerifySuccessView.as_view(), name='signup_success'),
    path('logout', views.UserLogoutView.as_view(), name='logout')
]