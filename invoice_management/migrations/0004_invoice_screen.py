# Generated by Django 4.0.6 on 2022-09-30 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_management', '0003_invoice_doctor_signature'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='screen',
            field=models.TextField(blank=True, null=True),
        ),
    ]
