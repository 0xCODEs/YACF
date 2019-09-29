# Generated by Django 2.1.8 on 2019-09-29 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified', models.BooleanField(default=False)),
                ('hidden', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('team', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='players', to='teams.Team')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
