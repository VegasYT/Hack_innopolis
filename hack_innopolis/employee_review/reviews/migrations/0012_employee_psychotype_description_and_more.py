# Generated by Django 5.1.2 on 2024-11-03 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0011_alter_generalsummary_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='psychotype_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='psychotype',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]