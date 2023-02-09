from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='jobs'),
    path('add', views.job_add, name='job_add'),
    path('<int:job_id>', views.job, name='job'),
    path('<int:job_id>/edit', views.job_edit, name='job_edit'),
]
