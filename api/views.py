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
