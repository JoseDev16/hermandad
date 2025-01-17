# Generated by Django 2.0 on 2018-11-08 06:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cargo', models.CharField(max_length=50)),
                ('tipo_cargo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CuentasPorCobrar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_cc', models.DateField()),
                ('tipo_cc', models.CharField(max_length=50)),
                ('monto_cc', models.FloatField()),
                ('concepto_cc', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hermandad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_hermandad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Medalla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Miembro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carnet', models.CharField(max_length=7)),
                ('nombre_m', models.CharField(max_length=100)),
                ('apellido_m', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=500)),
                ('fecha_nac', models.DateField()),
                ('estatura', models.FloatField()),
                ('num_contacto', models.CharField(max_length=15)),
                ('nombre_encargado', models.CharField(max_length=50)),
                ('parentesco', models.CharField(max_length=50)),
                ('num_encargado', models.CharField(max_length=15)),
                ('foto_m', models.ImageField(blank=True, upload_to='static/img')),
                ('cargo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='miembro.Cargo')),
                ('cuenta', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hermandad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='miembro.Hermandad')),
                ('medalla', models.ManyToManyField(to='miembro.Medalla')),
            ],
        ),
        migrations.CreateModel(
            name='Sacramento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sacramento', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Uniforme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='miembro',
            name='sacramentos',
            field=models.ManyToManyField(to='miembro.Sacramento'),
        ),
        migrations.AddField(
            model_name='miembro',
            name='uniformes',
            field=models.ManyToManyField(to='miembro.Uniforme'),
        ),
        migrations.AddField(
            model_name='cuentasporcobrar',
            name='miembro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='miembro.Miembro'),
        ),
    ]
