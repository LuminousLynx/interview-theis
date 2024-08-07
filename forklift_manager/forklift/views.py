from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseBase

from forklift.models import Forklift
import json

# Create your views here.
def overview(request: HttpRequest) -> HttpResponseBase:
    return render(request, 'forklift/overview.html', {
        'forklifts': Forklift.objects.all(),
    })


def toggle_operator(request: HttpRequest) -> HttpResponseBase:
    try:
        if request.method == 'PUT':
            
            data=json.loads(request.body)
            forklift_id = data.get("forklift_id")
            operator_id = data.get("operator_id")
            allowed = data.get("allowed")
            
            forklift = Forklift.objects.get(id=forklift_id)
            operators = list(forklift.allowed_operators)

            if allowed:
                operators.append(operator_id)
                print(operators)
            elif operator_id in operators:
                operators.remove(operator_id)

            forklift.allowed_operators = operators
            forklift.save(force_update=True)
            return HttpResponse()
        return HttpResponse("Request Method did not seem to be POST")
    except Exception as e:
        return HttpResponseBadRequest(e)
    

def can_operate(request: HttpRequest) -> HttpResponseBase:
    try:
        if request.method == 'PUT':
            
            data = json.loads(request.body)
            forklift_id = data.get("forklift_id")
            toggle = data.get("can_operate")

            forklift = Forklift.objects.get(id=forklift_id)

            if toggle:
                forklift.can_operate = 1
            else:
                forklift.can_operate = 0

            forklift.save(force_update=True)

            return HttpResponse()
        return HttpResponse("Request Method did not seem to be PUT")
    except Exception as e:
        return HttpResponseBadRequest(e)
    

def change_hours_run(request: HttpRequest) -> HttpResponseBase:
    try:

        return HttpResponse()
    except Exception as e:
        return HttpResponseBadRequest(e)