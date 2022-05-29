# Generated by Django 4.0.4 on 2022-05-29 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Autorlibro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autorid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autor.autor')),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('numeropagina', models.CharField(max_length=20)),
                ('editor', models.CharField(max_length=20)),
                ('isbn', models.CharField(max_length=20)),
                ('autorid', models.ManyToManyField(through='autor.Autorlibro', to='autor.autor')),
                ('ejemplaresid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.ejemplares')),
            ],
        ),
        migrations.AddField(
            model_name='autorlibro',
            name='libroid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autor.libro'),
        ),
    ]
