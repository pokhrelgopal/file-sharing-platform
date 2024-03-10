# Generated by Django 5.0.2 on 2024-03-10 16:36

import shortuuid.main
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0015_alter_favourite_id_alter_file_id_alter_invitation_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="invitation",
            name="message",
            field=models.TextField(blank=True, verbose_name="Message"),
        ),
        migrations.AlterField(
            model_name="favourite",
            name="id",
            field=models.CharField(
                default=shortuuid.main.ShortUUID.uuid,
                editable=False,
                max_length=22,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
        ),
        migrations.AlterField(
            model_name="file",
            name="id",
            field=models.CharField(
                default=shortuuid.main.ShortUUID.uuid,
                editable=False,
                max_length=22,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
        ),
        migrations.AlterField(
            model_name="invitation",
            name="id",
            field=models.CharField(
                default=shortuuid.main.ShortUUID.uuid,
                editable=False,
                max_length=22,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="id",
            field=models.CharField(
                default=shortuuid.main.ShortUUID.uuid,
                editable=False,
                max_length=22,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
        ),
        migrations.AlterField(
            model_name="organizationmember",
            name="id",
            field=models.CharField(
                default=shortuuid.main.ShortUUID.uuid,
                editable=False,
                max_length=22,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
        ),
    ]