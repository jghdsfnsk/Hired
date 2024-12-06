# Generated by Django 5.1.4 on 2024-12-06 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobs", "0003_alter_job_owner_alter_job_slug"),
    ]

    operations = [
        migrations.RenameField(
            model_name="job",
            old_name="description",
            new_name="fulldescription",
        ),
        migrations.AddField(
            model_name="job",
            name="summary",
            field=models.CharField(default="Something", max_length=100),
            preserve_default=False,
        ),
    ]