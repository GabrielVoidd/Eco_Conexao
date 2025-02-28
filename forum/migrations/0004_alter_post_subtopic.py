# Generated by Django 5.1.2 on 2024-10-15 02:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_alter_post_subtopic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subtopic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='forum.subtopic'),
        ),
    ]
