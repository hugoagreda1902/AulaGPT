# Generated by Django 5.2 on 2025-06-02 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_user_firebase_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='drive_folder_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
