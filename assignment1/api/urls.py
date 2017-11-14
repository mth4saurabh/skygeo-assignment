from django.conf.urls import url, include
from api import views
from rest_framework.routers import DefaultRouter


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'bookers', views.BookerViewSet)
router.register(r'bookings', views.BookingViewSet)
router.register(r'booking_items', views.BookingItemViewSet)
router.register(r'items', views.ItemViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'spaces', views.SpaceViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'venues', views.VenueViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
