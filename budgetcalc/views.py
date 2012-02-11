from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from mbta.budgetcalc.models import Category, Optiongroup, Option


def index(request):
    """
    Get everything.
    """
    options = Option.objects.select_related().all()
    return render_to_response('budgetcalc/index.html', locals(), context_instance=RequestContext(request))

