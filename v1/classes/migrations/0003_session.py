# Generated by Django 4.1.2 on 2022-11-11 08:35

import accounts.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('number', models.PositiveIntegerField(default=0)),
                ('video', models.FileField(blank=True, null=True, upload_to='classes/videos')),
                ('attachment', models.FileField(blank=True, null=True, upload_to='classes/attachment', validators=[accounts.validators.validate_file_size])),
                ('token', models.CharField(max_length=20, unique=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='classes.course')),
            ],
        ),
    ]
