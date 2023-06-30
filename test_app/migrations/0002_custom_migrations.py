from django.core.management import call_command
from django.db import migrations


def create_json_with_data(apps, schema_editor):
    call_command("fake_data")


def create_superuser(apps, schema_editor):
    call_command("create_superuser")


def load_to_db(apps, schema_editor):
    json_file = "/app/position_data.json"
    call_command("loaddata", json_file)


class Migration(migrations.Migration):

    dependencies = [
        ("test_app", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_json_with_data),
        migrations.RunPython(create_superuser),
        migrations.RunPython(load_to_db),
    ]
