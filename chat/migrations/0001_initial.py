# Generated by Django 5.1.3 on 2024-11-27 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=10000)),
                ('response', models.CharField(max_length=10000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
