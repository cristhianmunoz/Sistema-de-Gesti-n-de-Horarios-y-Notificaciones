# Generated by Django 4.1.7 on 2023-03-02 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_voluntarios', '0006_rename_horasexperiencia_habilidad_horas_experiencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voluntario',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
