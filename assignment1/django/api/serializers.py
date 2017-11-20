from rest_framework import serializers
from api.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'first_name', 'last_name', 'email', 'registered')


class BookerSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Bookers
        fields = ('id', 'user', 'created')


class BookingSerializer(serializers.ModelSerializer):
    booker = BookerSerializer(many=False, read_only=True)

    class Meta:
        model = Bookings
        fields = ('id', 'booker', 'created')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    item = serializers.HyperlinkedRelatedField(many=False, view_name='items-detail', read_only=True)

    class Meta:
        model = Products
        fields = ('id', 'item', 'price')


class SpaceSerializer(serializers.HyperlinkedModelSerializer):
    item = serializers.HyperlinkedRelatedField(many=False, view_name='items-detail', read_only=True)

    class Meta:
        model = Spaces
        fields = ('id', 'item', 'hour_price')


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venues
        fields = ('id', 'name')


class ItemSerializer(serializers.ModelSerializer):
    venue = VenueSerializer(many=False, read_only=True)

    class Meta:
        model = Items
        fields = ('id', 'name', 'venue')


class BookingItemSerializer(serializers.HyperlinkedModelSerializer):
    booking = BookingSerializer(many=False, read_only=True)
    item = ItemSerializer(many=False, read_only=True)

    class Meta:
        model = BookingItems
        fields = ('id', 'booking', 'item', 'quantity', 'locked_piece_price', 'locked_total_price', 'start_timestamp', 'end_timestamp')
