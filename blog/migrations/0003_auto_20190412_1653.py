# Generated by Django 2.1.7 on 2019-04-12 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_userimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='userimage',
            field=models.ImageField(default='default1.jpg', upload_to='profile_pics1'),
        ),
    ]
