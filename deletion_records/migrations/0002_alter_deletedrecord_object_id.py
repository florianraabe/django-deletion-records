from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("deletion_records", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="deletedrecord",
            name="object_id",
            field=models.CharField(verbose_name="object id"),
        ),
    ]
