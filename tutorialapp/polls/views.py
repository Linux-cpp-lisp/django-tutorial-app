from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from polls.models import Poll

def index(request):
    latest_polls = Poll.objects.order_by("-pub_date")[:5]
    return render(request, 'polls/index.html', {'latest_polls' : latest_polls})

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll' : poll})

def results(request, poll_id):
    return HttpResponse("Results of poll %s" % poll_id)

def vote(request, poll_id):
    return HttpResponse("Voting on poll %s" % poll_id)
