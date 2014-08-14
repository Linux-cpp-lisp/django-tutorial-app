from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world!")

def detail(request, poll_id):
    return HttpResponse("Details of poll %s" % poll_id)

def results(request, poll_id):
    return HttpResponse("Results of poll %s" % poll_id)

def vote(request, poll_id):
    return HttpResponse("Voting on poll %s" % poll_id)
