# Generated by Django 3.2.7 on 2022-11-18 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_remove_sms_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sms',
            old_name='title',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='sms',
            name='is_published',
        ),
    ]
