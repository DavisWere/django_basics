# Generated by Django 5.0.3 on 2024-03-29 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_books_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]