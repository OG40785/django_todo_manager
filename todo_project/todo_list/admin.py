from django.contrib import admin

from todo_list.models import ToDoItem
from todo_list.models import Category

@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = 'id','title','done','category_id'
    list_display_links = 'id', 'title','category_id'

@admin.register(Category)
class CategotyAdmin(admin.ModelAdmin):
    list_display = 'id','name'
    list_display_links = 'id', 'name'
