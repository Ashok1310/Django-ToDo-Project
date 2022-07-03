

from django.urls import path
from  . import views

app_name = "todo"
urlpatterns = [
    path('', views.index,name="home"),
    path('create', views.create_task,name="create"),
    path('<int:task_id>/update', views.update_task,name="update"),
    path('<int:task_id>/delete', views.delete_task,name="delete"),
]
