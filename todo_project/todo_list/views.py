from django.shortcuts import render

from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.views.generic import ListView,DetailView

from .models import ToDoItem
from .models import Category

def index_view(request: HttpRequest) -> HttpResponse:
    todo_items = ToDoItem.objects.order_by('-id').all()[:3]
    return render(
        request,
        template_name="todo_list/index.html",
        context={"todo_items": todo_items},
    )

class ToDoListView(ListView):
    #template_name = "todo_list/index.html"
    queryset = ToDoItem.objects.all()
    #we can avoid using context_object_name if change in templates todo_list
    #to object_list
    context_object_name = "todo_list"

    
    #def get_context_data(self, **kwargs):
       # print(ToDoItem._meta.app_label)
        #print(ToDoItem._meta.model_name)
       # return super().get_context_data(**kwargs)




    def get_context_data(self, **kwargs):
        # Get context from parent class
        context = super().get_context_data(**kwargs)

        # Add categories to the context
        context['categories'] = Category.objects.all()

        return context
    


class CategoriesView(ListView):
    template_name = "todo_list/categories_list.html"
    queryset = Category.objects.all()
    context_object_name = "categories"


class ToDoListDoneView(ListView):
    #template_name = "todo_list/done_list.html" 
    queryset = ToDoItem.objects.filter(done=True).all()
    context_object_name = "todo_list"

class ToDoDetailView(DetailView):
    model = ToDoItem