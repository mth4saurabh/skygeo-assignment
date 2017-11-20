# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bookers(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    created = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bookers'


class BookingItems(models.Model):
    id = models.IntegerField(primary_key=True)
    booking = models.ForeignKey('Bookings', models.DO_NOTHING)
    item = models.ForeignKey('Items', models.DO_NOTHING)
    quantity = models.IntegerField()
    locked_piece_price = models.FloatField()
    locked_total_price = models.FloatField()
    start_timestamp = models.IntegerField(blank=True, null=True)
    end_timestamp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_items'


class Bookings(models.Model):
    id = models.IntegerField(primary_key=True)
    booker = models.ForeignKey(Bookers, models.DO_NOTHING)
    created = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bookings'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Items(models.Model):
    id = models.IntegerField(primary_key=True)
    venue = models.ForeignKey('Venues', models.DO_NOTHING)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'items'


class Products(models.Model):
    id = models.IntegerField(primary_key=True)
    item = models.ForeignKey(Items, models.DO_NOTHING)
    price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'products'


class Spaces(models.Model):
    id = models.IntegerField(primary_key=True)
    item = models.ForeignKey(Items, models.DO_NOTHING)
    hour_price = models.FloatField()

    class Meta:
        managed = False
        db_table = 'spaces'


class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    registered = models.IntegerField()
    email = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'users'


class Venues(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'venues'
