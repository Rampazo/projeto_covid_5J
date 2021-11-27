# Generated by Django 3.2.9 on 2021-11-13 20:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20211113_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('import_file', models.BinaryField(verbose_name='Arquivo de Importação')),
            ],
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Perfil de Usuário', 'verbose_name_plural': 'Perfil de Usuários'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='create_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 13, 17, 40, 53, 862189), verbose_name='Data de Criação'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='update_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 13, 17, 40, 53, 862217), verbose_name='Data da Última Atualização'),
        ),
    ]
