# Generated by Django 4.1.3 on 2023-06-23 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_menu_menu_item_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='menu_item_description',
            new_name='description',
        ),
    ]
