# Generated by Django 2.2.5 on 2019-12-04 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('foto', models.FileField(blank=True, null=True, upload_to='banner')),
            ],
            options={
                'db_table': 'banner',
                'managed': False,
            },
        ),
    ]
