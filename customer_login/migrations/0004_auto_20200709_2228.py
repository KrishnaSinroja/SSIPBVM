# Generated by Django 3.0.8 on 2020-07-09 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_login', '0003_auto_20200709_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='contact',
            field=models.IntegerField(),
        ),
    ]
