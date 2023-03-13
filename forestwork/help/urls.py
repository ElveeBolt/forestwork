from django.urls import path
from . import views

urlpatterns = [
    path('faq', views.FaqListView.as_view(), name='faq'),
]