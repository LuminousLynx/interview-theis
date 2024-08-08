from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseBase

from forklift.models import Forklift, Repair
import json
import datetime

# Create your views here.
def overview(request: HttpRequest) -> HttpResponseBase:

    user = request.user
    
    if user.groups.filter(name="admin").exists():
        forklifts = Forklift.objects.all()
    elif user.groups.filter(name="Münster").exists():
        forklifts = Forklift.objects.filter(location="Münster")
    elif user.groups.filter(name="Berlin").exists():
        forklifts = Forklift.objects.filter(location="Berlin")
    elif user.groups.filter(name="Köln").exists():
        forklifts = Forklift.objects.filter(location="Köln")
    
    return render(request, 'forklift/overview.html', {
        'forklifts': forklifts,
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

#see if needed
def auto_check(request: HttpRequest) -> HttpResponseBase:
    try:
        if request.method == "PUT":

            #TO DO: implement
            return HttpRequest()
        return HttpResponse("This page has no content. The URL to this page is used automatically.")
    except Exception as e:
        return HttpResponseBadRequest(e)
    

def request_repair(request: HttpRequest) -> HttpResponseBase:
    try:
        if request.method == "PUT":

            data = json.loads(request.body)
            
            forklift_id = data.get("forklift_id")
            message = data.get("message")
            w1 = data.get("w1")
            w2 = data.get("w2")
            w3 = data.get("w3")

            if w1:
                workshop = 1
            elif w2:
                workshop = 2
            elif w3:
                workshop = 3

            repair = Repair()
            repair.workshop_id_id = workshop
            repair.model_id = forklift_id
            repair.message = message 

            repair.save()
            return HttpResponse()
        return HttpResponse("This page has no content. The URL to this page is used automatically.")
    except Exception as e:
        return HttpResponseBadRequest(e)
    
def end_repair(request: HttpRequest) -> HttpResponseBase:
    try:
        if request.method == "PUT":
            
            data = json.loads(request.body)
            
            forklift_id = data.get("forklift_id")
            price = data.get("price")

            repair = Repair.objects.get(active=True, model_id=forklift_id)

            end_date = datetime.date.today()
            formatted_end_date = end_date.strftime("%Y-%m-%d")
            start_date_list = str(repair.start_date).split("-")
            
            start_date = datetime.date(year=int(start_date_list[0]), month=int(start_date_list[1]), day=int(start_date_list[2]))
            
            repair_time = end_date - start_date
            
            repair.end_date = formatted_end_date
            repair.repair_cost = float(price)
            repair.repair_time = repair_time.days
            repair.active = False

            repair.save()

            return HttpResponse()
        return HttpResponse("This page has no content. The URL to this page is used automatically.")
    except Exception as e:
        return HttpResponseBadRequest(e)