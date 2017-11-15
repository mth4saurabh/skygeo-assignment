from rest_framework import serializers
from api.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'first_name', 'last_name', 'email', 'registered')


class BookerSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(many=False, view_name='users-detail', read_only=True)

    class Meta:
        model = Bookers
        fields = ('id', 'user', 'created')


class BookingItemSerializer(serializers.HyperlinkedModelSerializer):
    booking = serializers.HyperlinkedRelatedField(many=False, view_name='bookings-detail', read_only=True)
    item = serializers.HyperlinkedRelatedField(many=False, view_name='items-detail', read_only=True)

    class Meta:
        model = BookingItems
        fields = ('id', 'booking', 'item', 'quantity', 'locked_piece_price', 'locked_total_price', 'start_timestamp', 'end_timestamp')


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    booker = serializers.HyperlinkedRelatedField(many=False, view_name='bookers-detail', read_only=True)

    class Meta:
        model = Bookings
        fields = ('id', 'booker', 'created')


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    venue = serializers.HyperlinkedRelatedField(many=False, view_name='venues-detail', read_only=True)

    class Meta:
        model = Items
        fields = ('id', 'venue', 'name')


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