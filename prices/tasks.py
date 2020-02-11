# coding: utf-8

"""
Celery tasks
"""

from typing import Dict, List

import feedparser

from currencies import celery_app
from prices.models import Price


feed_urls = {
    'USD': 'https://www.ecb.europa.eu/rss/fxref-usd.html',
    'JPY': 'https://www.ecb.europa.eu/rss/fxref-jpy.html',
    'BGN': 'https://www.ecb.europa.eu/rss/fxref-bgn.html',
    'CZK': 'https://www.ecb.europa.eu/rss/fxref-czk.html',
    'DKK': 'https://www.ecb.europa.eu/rss/fxref-dkk.html',
    'EEK': 'https://www.ecb.europa.eu/rss/fxref-eek.html',
    'GBP': 'https://www.ecb.europa.eu/rss/fxref-gbp.html',
    'HUF': 'https://www.ecb.europa.eu/rss/fxref-huf.html',
    'PLN': 'https://www.ecb.europa.eu/rss/fxref-pln.html',
    'RON': 'https://www.ecb.europa.eu/rss/fxref-ron.html',
    'SEK': 'https://www.ecb.europa.eu/rss/fxref-sek.html',
    'CHF': 'https://www.ecb.europa.eu/rss/fxref-chf.html',
    'ISK': 'https://www.ecb.europa.eu/rss/fxref-isk.html',
    'NOK': 'https://www.ecb.europa.eu/rss/fxref-nok.html',
    'HRK': 'https://www.ecb.europa.eu/rss/fxref-hrk.html',
    'RUB': 'https://www.ecb.europa.eu/rss/fxref-rub.html',
    'TRY': 'https://www.ecb.europa.eu/rss/fxref-try.html',
    'AUD': 'https://www.ecb.europa.eu/rss/fxref-aud.html',
    'BRL': 'https://www.ecb.europa.eu/rss/fxref-brl.html',
    'CAD': 'https://www.ecb.europa.eu/rss/fxref-cad.html',
    'CNY': 'https://www.ecb.europa.eu/rss/fxref-cny.html',
    'HKD': 'https://www.ecb.europa.eu/rss/fxref-hkd.html',
    'IDR': 'https://www.ecb.europa.eu/rss/fxref-idr.html',
    'INR': 'https://www.ecb.europa.eu/rss/fxref-inr.html',
    'KRW': 'https://www.ecb.europa.eu/rss/fxref-krw.html',
    'MXN': 'https://www.ecb.europa.eu/rss/fxref-mxn.html',
    'MYR': 'https://www.ecb.europa.eu/rss/fxref-myr.html',
    'NZD': 'https://www.ecb.europa.eu/rss/fxref-nzd.html',
    'PHP': 'https://www.ecb.europa.eu/rss/fxref-php.html',
    'SGD': 'https://www.ecb.europa.eu/rss/fxref-sgd.html',
    'THB': 'https://www.ecb.europa.eu/rss/fxref-thb.html',
    'ZAR': 'https://www.ecb.europa.eu/rss/fxref-zar.html',
}


@celery_app.on_after_finalize.connect
def setup_periodic_tasks(sender, **_):
    """Set up periodic tasks
    """
    for currency, url in feed_urls.items():
        sender.add_periodic_task(10.0, scrap_rss.s(currency, url))


@celery_app.task
def scrap_rss(currency: str, url: str):
    """Read and insert into DB
    """
    data = read_rss(url)
    for entry in data:
        if not Price.objects.filter(currency=currency, timestamp=entry['timestamp']).exists():
            entry = Price(currency=currency, timestamp=entry['timestamp'], price=entry['price'])
            entry.save()


def read_rss(url: str) -> List[Dict[str, str]]:
    """Reading one RSS
    """
    data = feedparser.parse(url)
    return [{'price': e['cb_exchangerate'].split('\n')[0], 'timestamp': e['updated']} for e in data.entries]
