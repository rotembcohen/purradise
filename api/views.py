from .models import Game
from rest_framework import viewsets
from .serializers import GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Game.objects.all().order_by('-created_at')
    serializer_class = GameSerializer
    permission_classes = []
