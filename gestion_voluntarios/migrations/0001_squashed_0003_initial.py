# Generated by Django 4.1.7 on 2023-03-01 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('gestion_voluntarios', '0001_initial'), ('gestion_voluntarios', '0002_delete_voluntario'), ('gestion_voluntarios', '0003_initial')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Voluntario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=50)),
                ('apellido', models.CharField(default='', max_length=50)),
                ('edad', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diaSemana', models.CharField(choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miércoles', 'Miercoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sábado', 'Sabado'), ('Domingo', 'Domingo')], max_length=20)),
                ('horaInicio', models.TimeField()),
                ('horaFin', models.TimeField()),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='periodos', to='gestion_voluntarios.horario')),
            ],
        ),
        migrations.AddField(
            model_name='horario',
            name='voluntario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='horario', to='gestion_voluntarios.voluntario'),
        ),
        migrations.CreateModel(
            name='Habilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(choices=[('Suturar', 'Suturar'), ('Vacunar', 'Vacunar'), ('Anestesiar', 'Anestesiar')], max_length=20)),
                ('descripcion', models.CharField(default='', max_length=200)),
                ('horasExperiencia', models.PositiveIntegerField(default=0)),
                ('voluntario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_voluntarios.voluntario')),
            ],
        ),
    ]
