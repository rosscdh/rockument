# Generated by Django 3.1.7 on 2021-02-20 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponge', '0002_auto_20210219_2250'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='revision',
            unique_together={('app', 'revision')},
        ),
    ]