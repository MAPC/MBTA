from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.db.models import Avg, Count

import simplejson

from mbta.budgetcalc.models import Category, Optiongroup, Option, Submission


def index(request):
    """
    Get everything or save submission.
    """

    if request.method == 'GET':
        options = Option.objects.select_related().all()
        return render_to_response('budgetcalc/index.html', locals(), context_instance=RequestContext(request))
    elif request.method == 'POST':

        email = request.POST.get('email').lower()
        budget = float(request.POST.get('filled'))

        if Submission.objects.filter(email__icontains=email).exists():
            # update existing
            submission = Submission.objects.get(email=email)
            submission.budget = budget
            submission.options.clear()
        else:
            # create new
            submission = Submission(
                email=email,
                budget=budget
            )

        submission.save()

        options = simplejson.loads(request.POST['options'])
        for option in options:
            submission.options.add(Option.objects.get(pk=option))

        # some stats
        stats = Submission.objects.aggregate(Avg('budget'), Count('budget'))
        stats['options'] = dict()
        options = Option.objects.annotate(num_submissions=Count('selected_options'))
        for option in options:
            stats['options'][option.id] = option.num_submissions

        return HttpResponse(
                simplejson.dumps(stats),
                status=201,
                mimetype='application/json'
            )


def results(request):

    submissions = Submission.objects.select_related().all()
    submissions_count = submissions.count()

    options = Option.objects.annotate(num_submissions=Count('selected_options'))
    options_sorted = options.order_by('-num_submissions')

    # compiling chart data
    chart_values = simplejson.dumps([o.num_submissions for o in options_sorted])
    chart_titles = simplejson.dumps([o.title for o in options_sorted])

    return render_to_response('budgetcalc/results.html', locals(), context_instance=RequestContext(request))
