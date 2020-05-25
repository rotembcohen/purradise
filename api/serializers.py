from .models import Game
from rest_framework import serializers


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ['players_amount', 'address']
