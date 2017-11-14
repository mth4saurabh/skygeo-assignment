from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, detail_route
from api.models import *
from api.serializers import *



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'bookers': reverse('booker-list', request=request, format=format),
        'booking_items': reverse('booking_item-list', request=request, format=format),
        'bookings': reverse('booking-list', request=request, format=format),
        'items': reverse('item-list', request=request, format=format),
        'products': reverse('product-list', request=request, format=format),
        'spaces': reverse('space-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'venues': reverse('venue-list', request=request, format=format),
    })


class BookerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Bookers.objects.all()
    serializer_class = BookerSerializer


class BookingItemViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = BookingItems.objects.all()
    serializer_class = BookingItemSerializer


class BookingViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Bookings.objects.all()
    serializer_class = BookingSerializer


class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Items.objects.all()
    serializer_class = ItemSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class SpaceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Spaces.objects.all()
    serializer_class = SpaceSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class VenueViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Venues.objects.all()
    serializer_class = VenueSerializer