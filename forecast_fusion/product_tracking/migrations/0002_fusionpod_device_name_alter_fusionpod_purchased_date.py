# Generated by Django 4.2.7 on 2024-01-17 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_tracking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fusionpod',
            name='device_name',
            field=models.CharField(default='Device <django.db.models.fields.UUIDField>', max_length=60),
        ),
        migrations.AlterField(
            model_name='fusionpod',
            name='purchased_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
