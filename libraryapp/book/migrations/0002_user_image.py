# Generated by Django 3.1.7 on 2021-09-06 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='deafult.jpg', upload_to=''),
        ),
    ]
