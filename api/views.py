from .models import Game
from rest_framework import viewsets
from django.shortcuts import render
from django.views.generic import View
from .serializers import GameSerializer


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Game.objects.all().order_by('-created_at')
    serializer_class = GameSerializer
    permission_classes = []


class GetGamesView(View):
    def get(self, request):
        games = Game.objects.all()
        context = {"games": games}
        return render(request, "games.html", context)
