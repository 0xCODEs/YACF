# Generated by Django 2.1.2 on 2018-11-15 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_auto_20181115_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='solved',
            field=models.ManyToManyField(related_name='team', to='teams.SolvedChallenge'),
        ),
    ]
