# Generated by Django 2.0.5 on 2018-05-28 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_contact_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='drinks',
            field=models.IntegerField(default=0),
        ),
    ]
