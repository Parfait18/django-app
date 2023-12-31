# Generated by Django 4.1.12 on 2023-10-16 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.EmailField(error_messages={'unique': 'Email is already used'}, max_length=255, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('joined_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
