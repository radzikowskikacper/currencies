# coding: utf-8

"""
Views for currency exchange rate information
"""

import json

from django.http import HttpRequest, HttpResponseNotAllowed, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

from prices.models import Price


def get(request: HttpRequest, currency: str=None, date: str=None) -> HttpResponseNotAllowed or JsonResponse:
    """Get method for the rates views
    """
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])

    prices = Price.objects.all()
    if currency:
        prices = prices.filter(currency=currency)
    if date:
        prices = prices.filter(timestamp=date)
    prices = list(prices.values('currency', 'timestamp', 'price'))
    return JsonResponse(json.dumps(prices, cls=DjangoJSONEncoder), safe=False)
