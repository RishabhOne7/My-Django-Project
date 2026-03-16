
from django.urls import path , include
from Todo_app import views
urlpatterns = [

    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('services/',views.services,name='services'),
    path('todo_tasks/',views.todo_tasks,name='todo_tasks'),
    path('tasks_delet/<t_id>',views.tasks_delet,name='tasks_delet'),

    path('tasks_edit/<t_id>',views.tasks_edit,name='tasks_edit'),

]
