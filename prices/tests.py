# coding: utf-8

"""
Prices applications tests
"""

import json

from django.urls import reverse
import pytest


@pytest.mark.parametrize('url_namespace, arguments, answer', [
    ('prices', None, []),
    ('prices_of_currency', {'currency': 'PLN'}, []),
    ('price_per_date', {'currency': 'PLN', 'date': '2020-02-05T13:15:00Z'}, []),
])
@pytest.mark.django_db
def test_get(client, url_namespace, arguments, answer):
    if arguments is not None:
        response = client.get(reverse(url_namespace, kwargs=arguments))
    else:
        response = client.get(reverse(url_namespace))
    assert json.loads(response.json()) == answer
