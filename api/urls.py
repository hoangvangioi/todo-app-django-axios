from django.urls import path
from . import views
from .views import TaskListAPIView, TaskRetrieveAPIView, TaskDestroyAPIView, TaskCreateAPIView


urlpatterns = [
    path('', views.api, name = 'api'),
    path('task-update/<str:pk>/', views.taskUpdate, name = 'task_update'),
    path('task-list/', TaskListAPIView.as_view(), name = 'task_list'),
    path('task-detail/<str:pk>/', TaskRetrieveAPIView.as_view(), name = 'task_detail'),
    path('task-create/', TaskCreateAPIView.as_view(), name = 'task_create'),
    path('task-delete/<str:pk>/', TaskDestroyAPIView.as_view(), name = 'task_delete'),    
]