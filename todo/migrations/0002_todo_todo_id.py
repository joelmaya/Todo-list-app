# Generated by Django 2.2.5 on 2019-10-23 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='todo_id',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]