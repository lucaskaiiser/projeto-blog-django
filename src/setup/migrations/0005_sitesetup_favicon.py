# Generated by Django 5.1.6 on 2025-03-05 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0004_alter_menulink_setup'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesetup',
            name='favicon',
            field=models.ImageField(blank=True, default='', upload_to='assets/'),
        ),
    ]
