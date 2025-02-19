from django.urls import path
from . import views 
urlpatterns=[
    path('addtask/' , views.addTask , name="addtask"),
    path('mark_as_done/<int:pk>/' , views.mark_as_done , name='mark_as_done'),
    path('delete_task/<int:pk>/' , views.Delete_Task , name="delete_task"),
    path('mark_as_undone/<int:pk>/' , views.mark_as_undone , name='mark_as_undone'),
    path('update_task/<int:pk>/' , views.update_task , name='update_task'),
    
]