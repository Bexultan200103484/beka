# Generated by Django 4.0.3 on 2022-03-04 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_actor_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='content',
        ),
    ]
