# Generated by Django 3.2.9 on 2021-11-25 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyQuantityBad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_date', models.DateField(verbose_name='Data Inicial')),
                ('end_date', models.DateField(verbose_name='Data Final')),
                ('result_report', models.TextField(blank=True, null=True, verbose_name='Resultado')),
            ],
            options={
                'verbose_name': 'Quantidade Diária "Não muito bem"',
                'verbose_name_plural': 'Quantidades Diárias "Não muito bem"',
            },
        ),
    ]
