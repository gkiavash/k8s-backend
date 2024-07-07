from django.db import models


class Application(models.Model):
    name = models.CharField("name", max_length=150, null=True, blank=True)
