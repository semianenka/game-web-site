# Generated by Django 3.1.7 on 2021-03-10 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_auto_20210310_1000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='categories',
            new_name='genres',
        ),
    ]