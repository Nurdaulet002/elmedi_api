# Generated by Django 4.0.6 on 2022-07-23 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_management', '0002_alter_customerinsurance_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='surname',
            field=models.CharField(max_length=180, null=True),
        ),
    ]
