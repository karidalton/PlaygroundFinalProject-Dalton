# Generated by Django 5.0.2 on 2024-02-09 23:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_remove_venta_id_venta_operacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='categoria_id',
            new_name='categoria',
        ),
    ]