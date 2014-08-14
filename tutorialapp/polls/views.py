from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse

from polls.models import Poll, Choice

def index(request):
    latest_polls = Poll.objects.order_by("-pub_date")[:5]
    return render(request, 'polls/index.html', {'latest_polls' : latest_polls})

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll' : poll})

def results(request, poll_id):
    return HttpResponse("Results of poll %s" % poll_id)

def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    try:
        choice = poll.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'poll' : poll, 'error_message' : "You must select a choice."})
    else:
        choice.votes += 1
        choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(poll.id,)))
    
