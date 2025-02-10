from django.contrib import admin

from todo_list.models import ToDoItem
from todo_list.models import Category


@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = "id", "title", "visible_object", "done", "description", "category_id"
    list_display_links = "id", "title", "category_id"

    def visible_object(self, obj: ToDoItem) -> bool:
        return not obj.archived
    
    visible_object.boolean = True

@admin.register(Category)
class CategotyAdmin(admin.ModelAdmin):
    list_display = "id", "name"
    list_display_links = "id", "name"
