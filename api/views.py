from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import *
import json
from django.http import HttpResponse

require_http_methods(["POST"])
def postName(request):
    print(request.POST)
    obj = Name(name=request.POST.get("name"," "))
    obj.save()
    return HttpResponse(json.dumps({"name" : obj.name}), content_type="application/json")
