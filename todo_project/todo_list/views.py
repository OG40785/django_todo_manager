from django.shortcuts import render

from django.http import (
    HttpRequest,
    HttpResponse,
    HttpResponseRedirect,
)
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from .models import ToDoItem
from .models import Category
from .forms import TodoItemCreateForm
from .forms import TodoItemUpdateForm


def index_view(request: HttpRequest) -> HttpResponse:
    todo_items = ToDoItem.objects.order_by("-id").all()[:3]
    return render(
        request,
        template_name="todo_list/index.html",
        context={"todo_items": todo_items},
    )


class ToDoListView(ListView):
    # template_name = "todo_list/index.html"
    #queryset = ToDoItem.objects.all()
    queryset = ToDoItem.objects.filter(archived = False)
    # we can avoid using context_object_name if change in templates todo_list
    # to object_list
    context_object_name = "todo_list"

    # def get_context_data(self, **kwargs):
    # print(ToDoItem._meta.app_label)
    # print(ToDoItem._meta.model_name)
    # return super().get_context_data(**kwargs)

    def get_context_data(self, **kwargs):
        # Get context from parent class
        context = super().get_context_data(**kwargs)

        # Add categories to the context
        context["categories"] = Category.objects.all()

        return context


class CategoriesView(ListView):
    template_name = "todo_list/categories_list.html"
    queryset = Category.objects.all()
    context_object_name = "categories"


class ToDoListDoneView(ListView):
    # template_name = "todo_list/done_list.html"
    queryset = ToDoItem.objects.filter(done=True).all()
    context_object_name = "todo_list"


class ToDoDetailView(DetailView):
    model = ToDoItem


class TodoItemCreateView(CreateView):
    model = ToDoItem
    form_class = TodoItemCreateForm
    success_url = reverse_lazy("todo_list:list_of_todo")


class TodoItemUpdateView(UpdateView):
    model = ToDoItem
    form_class = TodoItemUpdateForm
    template_name_suffix='_update_form'
    success_url = reverse_lazy("todo_list:list_of_todo")

class TodoItemDeleteView(DeleteView):
    model = ToDoItem
  
    template_name_suffix='_delete_form'
    success_url = reverse_lazy("todo_list:list_of_todo")

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)
    
