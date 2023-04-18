# -*- coding: utf-8 -*-
# Generated by Django 4.0.5 on 2023-04-14 15:37

from django.db import migrations
from django.db import models
from django.db.models import F


def populate_numerical_phid(apps, schema_editor):
    Revision = apps.get_model("issues", "Revision")
    Revision.objects.all().update(numerical_phid=F("id"))


class Migration(migrations.Migration):
    dependencies = [
        ("issues", "0008_revision_base_head_references"),
    ]

    operations = [
        migrations.AddField(
            model_name="revision",
            name="numerical_phid",
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="revision",
            name="phid",
            field=models.CharField(blank=True, max_length=40, null=True, unique=True),
        ),
        migrations.RunPython(
            populate_numerical_phid,
            reverse_code=migrations.RunPython.noop,
            elidable=True,
        ),
        migrations.AlterField(
            model_name="revision",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
