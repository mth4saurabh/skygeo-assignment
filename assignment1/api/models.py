from django.db import models

class Venue(models.Model):
    name = models.CharField(max_length=100)


class Item(models.Model):
    name = models.CharField(max_length=100)
    venue_id = models.ForeignKey(Venue, related_name='items')


class Space(models.Model):
    hour_price = models.FloatField()
    item_id = models.ForeignKey(Item, related_name='spaces')


class Product(models.Model):
    price = models.FloatField()
    item_id = models.ForeignKey(Item, related_name='products')


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    registered = models.IntegerField(default=0)


class Booker(models.Model):
    created = models.IntegerField(default=0)
    user_id = models.ForeignKey(User, related_name='bookers')


class Booking(models.Model):
    created = models.IntegerField(default=0)
    booker_id = models.ForeignKey(Booker, related_name='bookings')


class BookingItem(models.Model):
    quantity = models.IntegerField()
    locked_piece_price = models.FloatField()
    locked_total_price = models.FloatField()
    start_timestamp = models.IntegerField(default=0)
    end_timestamp = models.IntegerField(default=0)
    booking_id = models.ForeignKey(Booking, related_name='booking_items')
    item_id = models.ForeignKey(Item, related_name='booking_items')
