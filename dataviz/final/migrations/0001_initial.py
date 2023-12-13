# Generated by Django 4.2.7 on 2023-12-04 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Final',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=255)),
                ('cases', models.IntegerField()),
                ('deaths', models.IntegerField()),
                ('region', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
            ],
            options={
                'db_table': 'final',
                'managed': False,
            },
        ),
    ]