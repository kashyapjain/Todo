# Generated by Django 4.1.2 on 2022-10-21 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('c', 'completed'), ('p', 'pending')], max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('priority', models.CharField(choices=[(4, 4), (1, 1), (6, 6), (3, 3), (7, 7), (8, 8), (5, 5), (9, 9), (2, 2)], max_length=2)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]