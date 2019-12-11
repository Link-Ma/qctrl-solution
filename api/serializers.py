from rest_framework import serializers
from .models import Control


class ControlSerializers(serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = ('name', 'type', 'maximum_rabi_rate', 'polar_angle',)
