# Generated by Django 4.0.1 on 2022-03-03 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_location_save_alter_location_end_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='save',
            new_name='save_bd',
        ),
    ]