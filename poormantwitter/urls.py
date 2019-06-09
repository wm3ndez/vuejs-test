from django.contrib import admin
from django.urls import path
from rest_framework import routers

from apps.twitter.views import index, TweetViewSet

router = routers.SimpleRouter()
router.register(r'tweets', TweetViewSet)

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
]

urlpatterns.extend(router.urls)
