# Generated by Django 5.1.5 on 2025-02-10 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0003_alter_category_options_todoitem_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
