# Generated by Django 4.1.4 on 2024-08-08 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forklift', '0008_repair_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='forklift',
            name='location',
            field=models.CharField(default='Münster', max_length=50),
        ),
    ]
