# encoding: utf-8

from django.views.generic.base import View
from goods.models import Goods
from django.http import HttpResponse, JsonResponse
import json
from django.core import serializers


class GoodsListView(View):
    def get(self, request):
        '''
        通过django的view实现商品列表页
        :param request:
        :return:
        '''
        json_list = []
        goods = Goods.objects.all()[:10]
        # for good in goods:
        #     json_dict = {}
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category.name
        #     json_dict['market_price'] = good.market_price
            # add_time会报错
            # json_dict['add_time'] = good.add_time
            # json_list.append(json_dict)

            # from django.forms.models import model_to_dict
            # for godd in goods:
            #     json_dict = model_to_dict(good)
            #     json_list.append(json_dict)
        # return HttpResponse(json.dumps(json_list), content_type='application/json')


        json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data)
        return JsonResponse(json_data, safe=False)

