from django.urls import path
from . import views

urlpatterns = [
    path('', views.JobListView.as_view(), name='jobs'),
    path('add', views.JobAddView.as_view(), name='job_add'),
    path('<int:pk>', views.JobDetailView.as_view(), name='job'),
    path('<int:pk>/edit', views.JobUpdateView.as_view(), name='job_edit'),
    path('<int:job_id>/delete', views.job_delete, name='job_delete'),
]
