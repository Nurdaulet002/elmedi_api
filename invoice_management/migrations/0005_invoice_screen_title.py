# Generated by Django 4.0.6 on 2023-03-27 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice_management', '0004_invoice_screen'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='screen_title',
            field=models.CharField(blank=True, max_length=180, null=True),
        ),
    ]
