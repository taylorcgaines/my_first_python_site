from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Question



# Create your views here.
def index (req):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, req))
def detail(req, question_id):
    # return HttpResponse("You're looking at question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(req, 'polls/detail.html', {'question': question})
def results(req, question_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)
def vote(req, question_id):
    return("You're voting on question %s." % question_id)
