# Generated by Django 3.0.6 on 2020-05-17 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0011_auto_20200517_2003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created',
            new_name='timestamp',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='moder',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='text',
        ),
        migrations.AddField(
            model_name='comment',
            name='context',
            field=models.TextField(default=1, max_length=120, verbose_name='текст комментария'),
            preserve_default=False,
        ),
    ]
