import json

from django.views.generic.base import View
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from django.core import serializers
# from django.views.generic import ListView

from goods.models import Goods


class GoodsListView(View):
    def get(self, request):
        """
        通过django的view实现商品列表页
        :param request:
        :return:
        """
        goods = Goods.objects.all()[:10]
        json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(json_data, safe=False)
