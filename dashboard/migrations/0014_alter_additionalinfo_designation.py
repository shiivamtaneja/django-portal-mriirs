# Generated by Django 4.1 on 2022-12-08 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_alter_researchpaper_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='additionalinfo',
            name='designation',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
