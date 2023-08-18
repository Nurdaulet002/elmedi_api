# Generated by Django 4.0.6 on 2022-07-21 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('directory', '0003_hospital_unicode'),
        ('referral_management', '0003_referral_cancel_date_referral_customer_and_more'),
        ('customer_management', '0002_alter_customerinsurance_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumption', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('performing_doctor', models.CharField(blank=True, max_length=180, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('type_appeal', models.IntegerField(choices=[(1, 'ОМС'), (2, 'ДМС'), (3, 'Платно')])),
                ('place', models.IntegerField(choices=[(1, 'На дому'), (2, 'ПМСП'), (3, 'Амбулаторно'), (4, 'Стационарно')])),
                ('customer_insurance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer_management.customerinsurance')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directory.hospital')),
                ('icd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directory.icd')),
                ('referral', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='referral_management.referral')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directory.service')),
            ],
        ),
    ]
