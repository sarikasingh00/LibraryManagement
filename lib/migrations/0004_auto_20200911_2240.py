# Generated by Django 3.0.2 on 2020-09-11 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0003_auto_20200911_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_image',
            field=models.ImageField(default='default.jpg', upload_to='book_pics'),
        ),
    ]
