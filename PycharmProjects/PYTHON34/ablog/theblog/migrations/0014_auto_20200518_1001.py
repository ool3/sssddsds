# Generated by Django 3.0.6 on 2020-05-18 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0013_auto_20200518_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Время комментария'),
        ),
    ]