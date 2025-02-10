from django import forms
from .models import ToDoItem
from django.utils.translation import gettext_lazy as _


class TodoItemCreateForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ("title", "description")  # Ensure these match the model fields

        labels = {
            "title": _("Title of the todo"),
            "description": "Description of the todo",
        }

        help_texts = {
            "title": _("Enter a unique name of the task."),
            "description": _("Enter a short description of the task."),
        }

        error_messages = {
            "description": {
                "max_length": _("This description is too long."),
            },
            "title": {
                "max_length": _("Thisname is too long."),
            },
        }

        widgets = {
            "description": forms.Textarea(attrs={"cols": 80, "rows": 20}),
        }

class TodoItemUpdateForm(forms.ModelForm):
    class Meta(TodoItemCreateForm.Meta):
        fields = ("title",'done', "description") 