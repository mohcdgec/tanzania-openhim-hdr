# Generated by Django 3.1.4 on 2021-01-20 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MasterData', '0002_icd10mapping'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facility',
            options={'verbose_name_plural': 'facilities'},
        ),
        migrations.AlterModelOptions(
            name='hdrexemptioncategory',
            options={'verbose_name_plural': 'hdr_exemption_categories'},
        ),
        migrations.AlterModelOptions(
            name='hdrpayercategory',
            options={'verbose_name_plural': 'hdr_payer_categories'},
        ),
    ]
