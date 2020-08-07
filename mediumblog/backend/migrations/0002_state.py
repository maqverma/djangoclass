# Generated by Django 3.1 on 2020-08-07 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('country_id', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'states',
                'managed': True,
            },
        ),
    ]