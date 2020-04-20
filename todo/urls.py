from django.urls import path
from.import views

urlpatterns = [
    path('home/', views.home,name='todo-home'),
    path('add/',views.addtodo,name='add'),
    path('complete/<todo_id>',views.todocompleted,name='complete'),
    path('delete/',views.delete_todo,name='delete'),
    path('deleteall/',views.delete_all,name='deleteall')
]