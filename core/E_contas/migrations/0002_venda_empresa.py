# Generated by Django 2.2.5 on 2019-11-24 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('E_contas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete='SET_NULL', to='E_contas.Empresa'),
            preserve_default=False,
        ),
    ]
