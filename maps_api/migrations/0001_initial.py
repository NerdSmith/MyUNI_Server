# Generated by Django 4.2.3 on 2023-07-19 14:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import maps_api.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core_api', '0008_alter_sublist_additional_course_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='Building title')),
                ('faculties', models.ManyToManyField(related_name='faculty_buildings', to='core_api.faculty')),
            ],
            options={
                'verbose_name': 'Building',
                'verbose_name_plural': 'Buildings',
            },
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(verbose_name='Floor')),
                ('map_file', models.FileField(blank=True, null=True, upload_to=maps_api.models.Map.get_map_path, validators=[django.core.validators.FileExtensionValidator(['png'])])),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='building_maps', to='maps_api.building')),
            ],
        ),
    ]
