from django.urls import path

from django.views.generic import TemplateView

from . import views

#name space - to put this name in navbar like todo_list:list_of_todo - the name of the view
app_name = 'todo_list'

urlpatterns = [
    #template view
    #path("", TemplateView.as_view(template_name="todo_list/index.html"), name = 'index'),

    #class based view
    path("", views.ToDoListView.as_view(), name = 'list_of_todo'),
]
