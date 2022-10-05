from datacenter.models import Passcard, format_duration
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits = []

    visits = Visit.objects.filter(leaved_at=None)
    for visit in visits:
        non_closed_visit = {
            'who_entered': visit.passcard,
            'entered_at': visit.entered_at,
            'duration': format_duration(visit.get_duration()),
            'is_strange': visit.is_visit_long(minutes=60)
        }
        non_closed_visits.append(non_closed_visit)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
