# Generated by Django 4.0.4 on 2022-11-22 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_session'),
    ]

    operations = [
        migrations.CreateModel(
            name='Broadcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_edited', models.BooleanField(default=False)),
                ('token', models.CharField(max_length=15)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='broadcast', to='classes.course')),
            ],
        ),
    ]