# Generated by Django 3.2.3 on 2021-05-19 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sendmail', '0004_auto_20210519_1238'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='Article',
        ),
    ]
