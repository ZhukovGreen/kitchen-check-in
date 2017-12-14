from datetime import datetime

from django.shortcuts import render

from .models import Employee, Lunch


def check_in(request):
    if request.method == 'GET':
        today = datetime.today()
        visitor_lunches = Lunch.objects.filter(date=today)
        feeded_visitors_ids = (
            visitor_lunches.
            values_list('employee__id', flat=True)
        )
        hungry_visitors = Employee.objects.exclude(
            id__in=feeded_visitors_ids,
        )
        feeded_visitors = Employee.objects.filter(
            id__in=feeded_visitors_ids,
        )
        pass  # just show the list of visitors + buttons
    elif request.method == 'POST':
        pass  # mark user that they had a lunch
    else:
        raise Exception(f'HTTP method {request.method} not allowed')

    ctx = {
        'date': today,
        'feeded_visitors': feeded_visitors,
        'hungry_visitors': hungry_visitors,
        'visitor_lunches': visitor_lunches,
    }
    return render(request, 'index.html', context=ctx)
