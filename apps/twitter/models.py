from django.db import models


class Tweet(models.Model):
    name = models.CharField(max_length=32)
    message = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']
