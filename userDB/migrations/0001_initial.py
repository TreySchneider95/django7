# Generated by Django 5.0.1 on 2024-01-02 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('dietary_preference', models.CharField(max_length=200)),
            ],
        ),
    ]
