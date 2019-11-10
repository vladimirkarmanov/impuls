# Generated by Django 2.2.6 on 2019-10-31 06:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20191031_1105'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalUserInfo',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='additional_info', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('country', models.CharField(default='Россия', max_length=30)),
                ('region', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('address', models.CharField(blank=True, max_length=120)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('mail_index', models.PositiveIntegerField(blank=True, null=True)),
                ('about', models.TextField(blank=True, max_length=500)),
            ],
        ),
    ]