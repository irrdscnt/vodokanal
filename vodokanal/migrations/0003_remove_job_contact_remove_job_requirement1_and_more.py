# Generated by Django 4.2.7 on 2023-11-26 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vodokanal', '0002_remove_job_description_job_contact_job_requirement1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='contact',
        ),
        migrations.RemoveField(
            model_name='job',
            name='requirement1',
        ),
        migrations.RemoveField(
            model_name='job',
            name='requirement2',
        ),
        migrations.RemoveField(
            model_name='job',
            name='requirement3',
        ),
        migrations.RemoveField(
            model_name='job',
            name='salary',
        ),
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
