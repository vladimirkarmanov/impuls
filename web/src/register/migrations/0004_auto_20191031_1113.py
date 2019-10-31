# Generated by Django 2.2.6 on 2019-10-31 06:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_additionaluserinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='job_position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='users', to='register.JobPosition'),
        ),
    ]
