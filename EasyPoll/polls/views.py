from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse


# Create your views here.

# ------------------- INDEX --------------------
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', { 'latest_question_list':latest_question_list } )

# ------------------- DETAIL -------------------
def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist!!")

    #shortchuts
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/detail.html', { 'question': question })
        
# ----------------- RESULTS -------------------
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', { 'question': question })


# ------------------ VOTE ---------------------
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(request.POST)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        # reverse() function helps avoid having to hardcode a URL in the view function.
        # this reverse() call will return a string like '/polls/3/results/'
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))