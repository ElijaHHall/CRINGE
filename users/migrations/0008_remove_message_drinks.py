# Generated by Django 2.0.5 on 2018-05-30 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_merge_20180529_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='drinks',
        ),
    ]
