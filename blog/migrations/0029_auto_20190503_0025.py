# Generated by Django 2.1 on 2019-05-02 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_auto_20190423_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Catagory',
            field=models.CharField(blank=True, choices=[('Goat', 'Goat'), ('Cow', 'Cow'), ('Birds', 'Birds'), ('Fishes', 'Fishes'), ('Farm Equipments', 'Farm Equipments'), ('Vegetables', 'Vegetables'), ('Flowers', 'Flowers'), ('Others..', 'Others..')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='district',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='state',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
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
