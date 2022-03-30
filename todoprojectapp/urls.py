from django.contrib import admin
from django.urls import path
from .views import home,login_view,logout_view
from .import views
from .import views_api

urlpatterns = [
    path('', home,name='home'),
    path('login',login_view,name="login"),
    path('logout',logout_view,name="logout"),
    path('register',views.register,name="register"),
    path('create',views.create,name="create"),
    path('todolist',views.todolist,name="todolist"),
    path('completed_todo',views.completed_todo,name="completed_todo"),
    path('edit/<int:pk>', views.edit),
    path('edit_todo', views.edit_todo, name='edit_todo'),
    path('delete/<int:pk>', views.delete),
    path('api/toto_api', views_api.TodoList.as_view()),
]