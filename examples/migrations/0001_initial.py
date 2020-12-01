# Generated by Django 3.1.3 on 2020-12-01 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TravelData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('mode_of_transport', models.IntegerField(choices=[(0, 'Automobile'), (1, 'Bicycle'), (2, 'Walking'), (3, 'Train'), (4, 'Subway'), (5, 'Other')])),
                ('miles_travelled', models.FloatField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='examples.location')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
