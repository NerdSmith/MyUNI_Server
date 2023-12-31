# Generated by Django 4.2.3 on 2023-07-20 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core_api', '0011_alter_coursegroup_options_and_more'),
        ('schedule_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='course_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_group_schedule', to='core_api.coursegroup'),
        ),
    ]
