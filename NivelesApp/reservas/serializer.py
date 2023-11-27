from rest_framework import serializers

from reservas.models import Reservas

class ReservasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservas
        fields = "__all__"

