# Generated by Django 2.1.7 on 2019-04-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20190415_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='userimage',
            field=models.ImageField(blank=True, default='default1.jpg', null=True, upload_to='postimage'),
        ),
        migrations.AlterField(
            model_name='post',
            name='userimage2',
            field=models.ImageField(blank=True, default='default1.jpg', null=True, upload_to='postimage'),
        ),
        migrations.AlterField(
            model_name='post',
            name='userimage3',
            field=models.ImageField(blank=True, default='default1.jpg', null=True, upload_to='postimage'),
        ),
    ]
