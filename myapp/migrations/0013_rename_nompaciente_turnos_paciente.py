# Generated by Django 4.1.6 on 2023-03-31 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_doctor_dni'),
    ]

    operations = [
        migrations.RenameField(
            model_name='turnos',
            old_name='nomPaciente',
            new_name='paciente',
        ),
    ]