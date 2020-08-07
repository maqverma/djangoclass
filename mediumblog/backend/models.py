from django.db import models

# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=255, unique=False)
    photo = models.CharField(max_length=255, unique=False)
    email = models.CharField(max_length=255, unique=False)
    mobile = models.CharField(max_length=255, unique=False)
    password = models.CharField(max_length=255, unique=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'users'


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.TextField(unique=False)
    content = models.TextField(unique=False)
    image = models.CharField(max_length=255, unique=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'acticles'


class State(models.Model):
    id = models.AutoField(primary_key=True)
    country_id = models.CharField(max_length=255, unique=False)
    state = models.CharField(max_length=255, unique=False)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'states'