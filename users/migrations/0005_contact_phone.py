# Generated by Django 2.0.5 on 2018-05-28 16:55

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_contact_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
    ]
