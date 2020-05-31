from django.shortcuts import render, redirect
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as log_out
from urllib.parse import urlencode
from django.conf import settings
from django.http import HttpResponseRedirect
from .models import Game
from rest_framework import viewsets
from .serializers import GameSerializer


def index(request):
    user = request.user
    if user.is_authenticated:
        return redirect("/codes")
    else:
        return render(request, "index.html")


def logout(request):
    log_out(request)
    return_to = urlencode({"returnTo": request.build_absolute_uri("/")})
    logout_url = "https://{}/v2/logout?client_id={}&{}".format(
        settings.SOCIAL_AUTH_AUTH0_DOMAIN, settings.SOCIAL_AUTH_AUTH0_KEY, return_to,
    )
    return HttpResponseRedirect(logout_url)


# class PostListView(View):
#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super(PostListView, self).dispatch(*args, **kwargs)
#
#     def get(self, request):
#         posts = Post.objects.all()
#         context = {"posts": posts}
#         return render(request, "home.html", context)


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
