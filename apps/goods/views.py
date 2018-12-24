from django.shortcuts import render
from .serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets

from .models import Goods
from .filters import GoodsFilter

# Create your views here.


# 定制分页
class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


# class GoodsListView(generics.ListAPIView):
class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'shop_price')
    filter_class = GoodsFilter
