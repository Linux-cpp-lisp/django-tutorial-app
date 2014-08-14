from django.shortcuts import render
from django.http import HttpResponse

from polls.models import Poll

def index(request):
    latest_polls = Poll.objects.order_by("-pub_date")[:5]
    return render(request, 'polls/index.html', {'latest_polls' : latest_polls})

def detail(request, poll_id):
    return HttpResponse("Details of poll %s" % poll_id)

def results(request, poll_id):
    return HttpResponse("Results of poll %s" % poll_id)

def vote(request, poll_id):
    return HttpResponse("Voting on poll %s" % poll_id)
