from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBadRequest, HttpResponseBase

from forklift.models import Forklift

# Create your views here.
def overview(request: HttpRequest) -> HttpResponseBase:
    return render(request, 'forklift/overview.html', {
        'forklifts': Forklift.objects.all(),
    })


def allow_operator(request: HttpRequest) -> HttpResponseBase:
    try:
        data = request.POST

        forklift = Forklift.objects.get(id=data['forklift_id'])
        operators = set(forklift.allowed_operators)

        if data['allowed'] == 'true':
            operators.add(int(data['operator_id']))
        elif data['operator_id'] in operators:
            operators.remove(int(data['operator_id']))

        forklift.allowed_operators = list(operators)
        forklift.save()
        return HttpResponse()
    except Exception as e:
        return HttpResponseBadRequest(e)
    

def can_operate(reguest: HttpRequest) -> HttpResponseBase:
    try:
        #TO DO: implement
        return HttpResponse()
    except Exception as e:
        return HttpResponseBadRequest(e)