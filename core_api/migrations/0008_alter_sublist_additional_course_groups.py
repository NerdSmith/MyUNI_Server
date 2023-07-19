# Generated by Django 4.2.3 on 2023-07-19 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_api', '0007_alter_coursegroup_subgroup_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sublist',
            name='additional_course_groups',
            field=models.ManyToManyField(limit_choices_to=models.Q(('id', models.F('sub_list_add_course_group')), _negated=True), related_name='sub_list_add_course_group', to='core_api.coursegroup'),
        ),
    ]