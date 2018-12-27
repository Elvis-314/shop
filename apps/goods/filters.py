#!/usr/bin/env python
# encoding: utf-8

import django_filters
from django.db.models import Q

from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤页
    """
    pricemin = django_filters.NumberFilter(name="shop_price", lookup_expr='gte')
    pricemax = django_filters.NumberFilter(name="shop_price", lookup_expr='lte')
    # icontains 中的i，表示忽略大小写,不带lookup_expr则要求全匹配
    # name = django_filters.CharFilter(name="name", lookup_expr='icontains')
    top_category = django_filters.NumberFilter(method='top_category_filter')


    # 查找第一分类下的商品
    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax']
