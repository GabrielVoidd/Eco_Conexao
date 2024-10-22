# Generated by Django 5.1.2 on 2024-10-15 02:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_alter_post_subtopic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subtopic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='forum.subtopic'),
        ),
    ]
