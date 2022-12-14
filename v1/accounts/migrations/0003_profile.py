# Generated by Django 4.0.4 on 2022-10-26 11:05

import accounts.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('picture', models.ImageField(upload_to='users/pictures', validators=[accounts.validators.validate_file_size])),
                ('age', models.SmallIntegerField(validators=[django.core.validators.MaxValueValidator(60), django.core.validators.MinValueValidator(10)])),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Phone number format must be like: (XXX) XXX XXXX', regex='\\(?\\d{3}\\)?-? *\\d{3}-? *-?\\d{4}')])),
                ('address', models.CharField(max_length=300)),
                ('passport_number', models.CharField(max_length=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
