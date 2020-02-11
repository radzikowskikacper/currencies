# coding: utf-8

"""
Prices applications URLs
"""

from django.urls import path

from . import views


urlpatterns = [
    path(r'', views.get, name='prices'),
    path(r'<str:currency>/', views.get, name='prices_of_currency'),
    path(r'<str:currency>/<str:date>/', views.get, name='price_per_date'),
]
