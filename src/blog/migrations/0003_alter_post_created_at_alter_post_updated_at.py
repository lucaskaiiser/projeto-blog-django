# Generated by Django 5.1.6 on 2025-03-08 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_excert'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
