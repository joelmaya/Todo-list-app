# Generated by Django 2.2.5 on 2019-10-23 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_todo_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='todo_id',
        ),
    ]
