from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from apps.twitter.models import Tweet
from apps.twitter.serializers import TweetSerializer


def index(request):
    return render(request, 'index.html')


class TweetViewSet(ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
