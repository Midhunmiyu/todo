# Generated by Django 4.1.5 on 2023-02-03 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='remindr',
            new_name='reminder',
        ),
    ]
