# coding: utf-8

"""
Django's command-line utility for administrative tasks.
"""

from django.db import models


class Price(models.Model):
    """Model for a currency price
    """

    currency = models.CharField(max_length=5)
    timestamp = models.DateTimeField()
    price = models.FloatField()
