import json

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from abs.models import Abs


class MainView(View):
    def get(self, request):
        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class AbsView(View):
    def get(self, request):
        ads = Abs.objects.all()
        response = []

        for ads_item in ads:
            response.append({
                "id": ads_item.id,
                "name": ads_item.name,
                "author": ads_item.author,
                "price": ads_item.price,
                "description": ads_item.description,
                "address": ads_item.address,
                "is_published": ads_item.is_published,
            })

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request):
        ads_data = json.loads(request.body)
        ads = Abs()

        ads.id = ads_data["id"]
        ads.name = ads_data["name"]
        ads.author = ads_data["author"]
        ads.price = ads_data["price"]
        ads.description = ads_data["price"]
        ads.is_published = ads_data.get("is_published", False)

        try:
            ads.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        ads.save()

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published,
        }, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class AdsEntityView(View):
    def get(self, request, pk):
        ads = get_object_or_404(Abs, id=pk)

        return JsonResponse({
            "id": ads.id,
            "name": ads.name,
            "author": ads.author,
            "status": ads.status,
            "price": ads.price,
            "description": ads.description,
            "address": ads.address,
            "is_published": ads.is_published,
        }, json_dumps_params={"ensure_ascii": False})