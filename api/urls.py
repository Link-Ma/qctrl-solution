from django.conf.urls import include, url
from django.urls import path, include
from rest_framework import routers
from api.views import ControlViewSet
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

# Default router.
route = routers.DefaultRouter()

# Register new address.
route.register('control', ControlViewSet)

# Register root level address.
urlpatterns = [
    url('api/', include(route.urls)),
]
