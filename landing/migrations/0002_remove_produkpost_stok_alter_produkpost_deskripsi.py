# Generated by Django 5.2 on 2025-05-09 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("landing", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="produkpost",
            name="stok",
        ),
        migrations.AlterField(
            model_name="produkpost",
            name="deskripsi",
            field=models.TextField(default="Belum Ada Deskripsi"),
            preserve_default=False,
        ),
    ]
