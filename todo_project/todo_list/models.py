from django.db import models


class Category(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name = "Categorie"

    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ToDoItem(models.Model):
    class Meta:
        ordering = ["id"]
        verbose_name = "ToDo Item"

    title = models.CharField(max_length=50,unique=True)
    done = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=False)
    category_id = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title
