# Generated by Django 2.1.7 on 2019-04-18 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20190418_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='userimage',
            field=models.ImageField(default='default1.jpg', null=True, upload_to='postimage'),
        ),
        migrations.AlterField(
            model_name='post',
            name='userimage2',
            field=models.ImageField(default='default1.jpg', null=True, upload_to='postimage'),
        ),
        migrations.AlterField(
            model_name='post',
            name='userimage3',
            field=models.ImageField(default='default1.jpg', null=True, upload_to='postimage'),
        ),
    ]
