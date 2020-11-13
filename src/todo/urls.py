from django.urls import path
from .views import list_create_tasks, update_task, delete_task

urlpatterns = [
    path('', list_create_tasks, name='list_tasks'),
    path('update/<int:id>/', update_task, name='update_task'),
    path('delete/<int:id>/', delete_task, name='delete_task'),
]