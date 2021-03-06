# Generated by Django 3.0.1 on 2019-12-25 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20191225_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default='Black', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='main_product_category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='material',
            field=models.CharField(default='Material', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='offers',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default='M', max_length=10),
        ),
    ]
