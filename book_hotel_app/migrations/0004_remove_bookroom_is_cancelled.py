# Generated by Django 5.0 on 2023-12-19 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_hotel_app', '0003_alter_room_name_room_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookroom',
            name='is_cancelled',
        ),
    ]
