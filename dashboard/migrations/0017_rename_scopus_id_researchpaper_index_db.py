# Generated by Django 4.1 on 2023-01-09 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0016_researchpaper_domain'),
    ]

    operations = [
        migrations.RenameField(
            model_name='researchpaper',
            old_name='scopus_id',
            new_name='index_db',
        ),
    ]