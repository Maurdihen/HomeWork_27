import json

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from categories.models import Categories


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesView(View):
    def get(self, request):
        categories = Categories.objects.all()
        response = []

        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name,
            })

        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

    def post(self, request):
        category_data = json.loads(request.body)
        category = Categories()

        category.id = category_data["id"]
        category.name = category_data["name"]

        try:
            category.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        category.save()

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        }, json_dumps_params={"ensure_ascii": False})

@method_decorator(csrf_exempt, name='dispatch')
class CategoriesEntityView(View):
    def get(self, request, pk):
        category = get_object_or_404(Categories, id=pk)

        return JsonResponse({
            "id": category.id,
            "name": category.name,
        }, json_dumps_params={"ensure_ascii": False})