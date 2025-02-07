from django.shortcuts import render

from django.views.generic import ListView

from .models import ToDoItem


class ToDoListView(ListView):
    template_name = "todo_list/index.html"
    queryset = ToDoItem.objects.all()
    context_object_name = "todo_list"
