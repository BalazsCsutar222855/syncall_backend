# Generated by Django 4.2.6 on 2023-10-21 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editor_core', '0002_page_is_favorite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='is_favorite',
            new_name='favorite',
        ),
    ]