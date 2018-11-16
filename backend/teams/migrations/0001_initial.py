# Generated by Django 2.1.2 on 2018-11-16 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('challenges', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SolvedChallenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('challenge', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='challenges.Challenge')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('hidden', models.BooleanField(default=False)),
                ('wrong_flags', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('accesscode', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='solvedchallenge',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solved', to='teams.Team'),
        ),
        migrations.AddField(
            model_name='solvedchallenge',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
