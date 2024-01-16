# Generated by Django 5.0.1 on 2024-01-10 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crystal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('appearance', models.TextField(max_length=500)),
                ('rarity', models.CharField(max_length=100)),
                ('source', models.TextField(max_length=250)),
            ],
        ),
    ]
