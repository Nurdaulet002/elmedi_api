# Generated by Django 4.0.6 on 2022-07-23 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_management', '0003_alter_customer_surname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=180, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='national',
            field=models.CharField(blank=True, max_length=180, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='place_work',
            field=models.CharField(blank=True, max_length=180, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='profession',
            field=models.CharField(blank=True, max_length=180, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='surname',
            field=models.CharField(blank=True, max_length=180, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='telephone_number',
            field=models.CharField(blank=True, max_length=180, null=True),
        ),
    ]
