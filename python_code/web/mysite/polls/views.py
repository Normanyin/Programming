from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from polls.models import Poll
from django.http  import Http404
# Create your views here.

def index(request):
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = Context({
		'latest_poll_list':latest_poll_list,
	})
#	return HttpResponse(template.render(context))
	return render(request, 'polls/index.html', {'latest_poll_list':latest_poll_list})

def detail(request, poll_id):
	try:
		poll = Poll.objects.get(pk=poll_id)
	except Poll.DoesNotExist:
		raise Http404
	return render(reques, 'polls/detail.html', {'poll':poll})

def results(request, poll_id):
        return HttpResponse("You are looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
        return HttpResponse("You are voting on poll%s." % poll_id)
