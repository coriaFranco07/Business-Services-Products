# Generated by Django 4.2.4 on 2023-10-17 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='categorias',
        ),
        migrations.AddField(
            model_name='empleado',
            name='categorias',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='empleados.categoriaempleado'),
        ),
    ]