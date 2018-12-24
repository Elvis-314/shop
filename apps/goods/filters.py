#!/usr/bin/env python
# encoding: utf-8

import django_filters
from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤页
    """
    price_min = django_filters.NumberFilter(name="shop_price", lookup_expr='gte')
    price_max = django_filters.NumberFilter(name="shop_price", lookup_expr='lte')
    # icontains 中的i，表示忽略大小写,不带lookup_expr则要求全匹配
    # name = django_filters.CharFilter(name="name", lookup_expr='icontains')
    class Meta:
        model = Goods
        fields = ['price_min', 'price_max']
