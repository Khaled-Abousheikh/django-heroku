from django.db import models


class Query(models.Model):
    query = models.CharField(max_length=255)
    text_str = models.CharField(max_length=255, blank=True)
