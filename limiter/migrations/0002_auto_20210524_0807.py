# Generated by Django 3.2.3 on 2021-05-24 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('limiter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='time_to_complete',
        ),
        migrations.CreateModel(
            name='UserProcessQueue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_to_complete', models.IntegerField(default=1)),
                ('time_completed', models.IntegerField(default=1)),
                ('is_stopped', models.BooleanField(default=False)),
                ('is_finished', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='process', to='limiter.users')),
            ],
        ),
    ]
