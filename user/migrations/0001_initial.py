# Generated by Django 3.2.9 on 2021-11-13 19:18

import datetime
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
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('user_type', models.CharField(choices=[('STUDENT', 'Estudante'), ('TEACHER', 'Professor'), ('STAFF', 'Funcionario')], max_length=20, verbose_name='Tipo de Usuário')),
                ('birth_date', models.DateField(verbose_name='Data de Nascimento')),
                ('city', models.CharField(max_length=50, verbose_name='Cidade')),
                ('state', models.CharField(max_length=2, verbose_name='UF')),
                ('create_at', models.DateTimeField(default=datetime.datetime(2021, 11, 13, 16, 18, 6, 243998), verbose_name='Data de Criação')),
                ('update_at', models.DateTimeField(default=datetime.datetime(2021, 11, 13, 16, 18, 6, 244023), verbose_name='Data da Última Atualização')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
    ]
