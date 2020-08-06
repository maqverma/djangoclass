# Generated by Django 3.1 on 2020-08-05 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('heading', models.TextField()),
                ('content', models.TextField()),
                ('image', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'acticles',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=255)),
                ('photo', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'users',
                'managed': True,
            },
        ),
    ]