# Generated by Django 4.2.6 on 2023-10-25 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['name'], 'verbose_name': 'Mi departamento', 'verbose_name_plural': 'Mis departamentos'},
        ),
        migrations.AlterUniqueTogether(
            name='departamento',
            unique_together={('name', 'shor_name')},
        ),
    ]
