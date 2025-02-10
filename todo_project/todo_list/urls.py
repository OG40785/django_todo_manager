from django.urls import path

from django.views.generic import TemplateView

from . import views

#name space - to put this name in navbar like todo_list:list_of_todo - the name of the view
app_name = 'todo_list'

urlpatterns = [
    #template view
    #path("", TemplateView.as_view(template_name="todo_list/index.html"), name = 'index'),


    # path("", views.index_view, name="index"),

    #class based view
    path("", views.ToDoListView.as_view(), name = 'list_of_todo'),
    path("categories", views.CategoriesView.as_view(), name = 'categories'),
    path("done/", views.ToDoListDoneView.as_view(), name = 'done'),
    path("<int:pk>/", views.ToDoDetailView.as_view(), name="detail"),
    path("create/", views.TodoItemCreateView.as_view(), name="create"),
    path("<int:pk>/update/", views.TodoItemUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.TodoItemDeleteView.as_view(), name="delete"),
]
