# Generated by Django 3.1.4 on 2021-01-11 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MasterData', '0007_auto_20210105_0632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientmetadata',
            name='client_id',
        ),
        migrations.AddField(
            model_name='clientmetadata',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MasterData.client'),
        ),
        migrations.AddField(
            model_name='eventmetadata',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MasterData.event'),
        ),
    ]
