# Generated by Django 5.1.2 on 2024-11-02 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_aspect_created_at_aspectsummary_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aspect',
            name='created_at',
        ),
    ]