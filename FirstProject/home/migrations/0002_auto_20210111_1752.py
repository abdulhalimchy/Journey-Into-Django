# Generated by Django 3.1.5 on 2021-01-11 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='message',
            new_name='msg',
        ),
    ]
