# Generated by Django 5.1 on 2024-08-21 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0003_rename_photo_profile_foto_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='pais',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='genero',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='foto',
            new_name='photo',
        ),
    ]
