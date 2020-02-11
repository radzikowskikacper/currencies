# coding: utf-8

"""
Main application module
"""

from .celery import app as celery_app


__all__ = [
    'asgi',
    'settings',
    'urls',
    'wsgi',

    'celery_app'
]
