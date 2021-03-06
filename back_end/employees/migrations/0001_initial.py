# Generated by Django 3.2.7 on 2021-09-13 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, unique=True)),
                ('gender', models.CharField(max_length=15, null=True)),
                ('date_of_birth', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('role', models.CharField(max_length=50, null=True)),
                ('status', models.CharField(max_length=30, null=True)),
                ('joining_date', models.CharField(max_length=20, null=True)),
                ('designation', models.CharField(max_length=40, null=True)),
                ('phone_no', models.CharField(max_length=11, null=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
            ],
        ),
    ]
