# Generated by Django 2.1.7 on 2019-04-12 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='userimage',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]