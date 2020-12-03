# Generated by Django 2.1.3 on 2020-12-03 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json', models.TextField()),
                ('date_deleted', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'client',
            },
        ),
        migrations.CreateModel(
            name='ClientMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('document_id', models.TextField()),
                ('date_deleted', models.DateTimeField(blank=True, null=True)),
                ('client_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MasterData.Client')),
            ],
            options={
                'db_table': 'client_metadata',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json', models.TextField()),
                ('date_deleted', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='EventMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(blank=True, max_length=255, null=True)),
                ('event_date', models.DateTimeField(blank=True, null=True)),
                ('server_version', models.TextField()),
                ('document_id', models.TextField()),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('date_edited', models.DateTimeField(blank=True, null=True)),
                ('date_deleted', models.DateTimeField(blank=True, null=True)),
                ('client_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MasterData.Client')),
                ('event_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MasterData.Event')),
            ],
            options={
                'db_table': 'event_metadata',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json', models.TextField()),
                ('active', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'location',
            },
        ),
        migrations.CreateModel(
            name='LocationMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('parent_id', models.TextField()),
                ('uuid', models.TextField()),
                ('status', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('version', models.TextField()),
                ('latitude', models.CharField(max_length=255)),
                ('longitude', models.CharField(max_length=255)),
                ('location_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MasterData.Location')),
            ],
            options={
                'db_table': 'location_metadata',
            },
        ),
        migrations.CreateModel(
            name='LocationTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('active', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'location_tag',
            },
        ),
        migrations.CreateModel(
            name='LocationTagMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MasterData.Location')),
                ('location_tag_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MasterData.LocationTag')),
            ],
            options={
                'db_table': 'location_tag_map',
            },
        ),
    ]
