# Generated by Django 2.1 on 2018-08-23 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_user_is_tutor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_tutor',
        ),
    ]
