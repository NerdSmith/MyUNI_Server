# Generated by Django 4.2.3 on 2023-07-20 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core_api', '0010_sublist_wvs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Subject title')),
                ('note', models.CharField(max_length=100, verbose_name='Additional text')),
                ('direction', models.ManyToManyField(related_name='subject_directions', to='core_api.direction')),
            ],
        ),
        migrations.CreateModel(
            name='InfoPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Post title')),
                ('subtitle', models.CharField(max_length=100, verbose_name='Post subtitle')),
                ('source_url', models.URLField(blank=True, max_length=100, verbose_name='Post source url')),
                ('content', models.CharField(blank=True, max_length=10000, verbose_name='Post content')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info_post_subject', to='manual_api.subject')),
            ],
        ),
    ]
