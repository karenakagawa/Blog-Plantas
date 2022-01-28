# Generated by Django 3.2.8 on 2021-12-02 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuidado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qntdAdubacao', models.CharField(max_length=50)),
                ('dataAdubacao', models.DateField()),
                ('dataRega', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Especies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeEspecie', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('sobrenome', models.CharField(max_length=30)),
                ('dt_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('cuidador', models.CharField(help_text='Explique a quanto tempo é cuidador de plantas', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_popular', models.CharField(max_length=50)),
                ('nomeCientifico', models.CharField(max_length=50)),
                ('dataPlantio', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Sugestoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
            ],
        ),
    ]
