# Generated by Django 2.1 on 2019-04-23 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20190418_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='userimage',
            field=models.ImageField(default=False, null=True, upload_to='postimage'),
        ),
        migrations.AlterField(
            model_name='post',
            name='userimage2',
            field=models.ImageField(default=False, null=True, upload_to='postimage'),
        ),
        migrations.AlterField(
            model_name='post',
            name='userimage3',
            field=models.ImageField(default=False, null=True, upload_to='postimage'),
        ),
    ]
