from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseBase

from forklift.models import Forklift
import json
import datetime

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
            elif operator_id in operators:
                operators.remove(operator_id)

            forklift.allowed_operators = operators
            forklift.save(force_update=True)
            return HttpResponse()
        return HttpResponse("This page has no content. The URL to this page is used automatically.")
    except Exception as e:
        return HttpResponseBadRequest(e)
    

def can_operate(request: HttpRequest) -> HttpResponseBase:
    try:
        if request.method == 'PUT':
            
            data = json.loads(request.body)
            forklift_id = data.get("forklift_id")
            toggle = data.get("can_operate")

            forklift = Forklift.objects.get(id=forklift_id)
            
            forklift.can_operate = toggle
            forklift.save(force_update=True)

            return HttpResponse()
        return HttpResponse("This page has no content. The URL to this page is used automatically.")
    except Exception as e:
        return HttpResponseBadRequest(e)
    

def update_hours_run(request: HttpRequest) -> HttpResponseBase:
        
    if request.method == 'PUT':
        try:

            data = json.loads(request.body)
            forklift_id = data.get("forklift_id")
            added_time = data.get("added_time")

            forklift = Forklift.objects.get(id=forklift_id)
            forklift.hours_run += float(added_time)
            forklift.hours_run = round(forklift.hours_run, 1)
            forklift.save()

            return HttpResponse()
        except Exception as e:
            return HttpResponseBadRequest(e)
    return HttpResponse("This page has no content. The URL to this page is used automatically.")
    
    
def update_next_check(request: HttpRequest) -> HttpResponseBase:
    try:
        if request.method == 'PUT':
            
            data = json.loads(request.body)
            forklift_id = data.get("forklift_id")
            next_check = data.get("next_check")
            
            date_list = next_check.split(".")
            new_date = date_list[2]+"-"+date_list[1]+"-"+date_list[0]

            forklift = Forklift.objects.get(id=forklift_id)

            forklift.next_check = new_date
            forklift.save()

            return HttpResponse()
        return HttpResponse("This page has no content. The URL to this page is used automatically.")
    except Exception as e:
        return HttpResponseBadRequest(e)