# Generated by Django 5.1.1 on 2024-09-19 06:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0001_initial'),
        ('thread', '0003_alter_discussionthread_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussionthread',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='subject.subject'),
        ),
    ]
