# Generated by Django 2.0 on 2017-12-14 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('check_in', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='lunch',
            unique_together={('employee', 'date')},
        ),
    ]
