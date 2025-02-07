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

    title = models.CharField(max_length=50)
    done = models.BooleanField(default=False)
    category_id = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.title
