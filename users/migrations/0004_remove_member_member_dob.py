# Generated by Django 3.0.5 on 2020-09-08 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200908_2232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='member_dob',
        ),
    ]