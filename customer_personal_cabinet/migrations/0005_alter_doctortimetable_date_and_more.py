# Generated by Django 4.0.6 on 2022-10-13 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_personal_cabinet', '0004_doctor_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctortimetable',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='doctortimetable',
            name='time',
            field=models.TimeField(),
        ),
    ]
