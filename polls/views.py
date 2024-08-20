from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from . models import Question, Choice

# Create your views here.
def index(request):
    return render(request,"pages/index.html")

def polls(request):
    # question = get_object_or_404(Question, id = question_id)
    questions ={}
    questions["questions"]= Question.objects.all()
    print(questions["questions"])
    context = {
        "questions": questions["questions"],
    }
    return render(request, "pages/polls.html", context)

def choices(request,question_id):
    question = get_object_or_404(Question, id= question_id)
    print("choices")
    context = {
        "question": question,
    }
    return render(request, "pages/choices.html", context)

def results(request,question_id):
    question = get_object_or_404(Question, id= question_id)
    print("results")
    context = {
        "question": question,
    }
    return render(request, "pages/results.html", context)
def votes(request,question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        context ={
            'question': question,
            'msg': "You didn't select any choice",
        }
        return render(request, "pages/choices.html",{'question': question,
            'msg': "You didn't select any choice",})
    else:

        print(selected_choice)
        selected_choice.votes +=1
        selected_choice.save()
        print(selected_choice.votes)
    return HttpResponseRedirect(reverse('results', args =(question.id, )))


