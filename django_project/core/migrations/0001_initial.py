# Generated by Django 3.2.5 on 2021-07-04 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=200)),
                ('status', models.CharField(default='pending', max_length=100, verbose_name=[('pending', 'PENDING'), ('Completed', 'COMPLETED')])),
            ],
        ),
    ]
