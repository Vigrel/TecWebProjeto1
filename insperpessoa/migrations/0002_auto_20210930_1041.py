# Generated by Django 3.2.7 on 2021-09-30 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insperpessoa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insperpessoa',
            name='nome',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='insperpessoa',
            name='sobrenome',
            field=models.CharField(max_length=200),
        ),
    ]