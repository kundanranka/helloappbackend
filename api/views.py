from django.http.response import JsonResponse

from django.views.decorators.http import require_http_methods
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse

@csrf_exempt
def postName(request):
    if request.method == "POST":
        data = json.loads(request.body)
        obj = Name(name=data.get("name"," "))
        obj.save()
        return JsonResponse({"name" : obj.name})

#TODO : Code Standard Extention Python/Django
#TODO : DAO layer for Django
#TODO : Dockerfile for Django
#TODO : Layered Architecture
#TODO : MySQL DB Migration
#TODO : Table naming convenstion standards
#TODO : Swagger API Docs for Django
#TODO : Look into https://www.envoythere.com/
