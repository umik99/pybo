from django.shortcuts import render, get_object_or_404, redirect
from ..models import Question, Answer
from django.http import HttpResponseNotAllowed
from django.utils import timezone
from ..forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def index(request):
    page = request.GET.get('page','1') #페이지
    kw = request.GET.get('kw','') #검색어
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw)|
            Q(content__icontains=kw)|
            Q(answer__content__icontains=kw)|
            Q(author__username__icontains=kw)|
            Q(answer__author__username__icontains=kw)
        ).distinct()
    paginator = Paginator(question_list,10) #페이지당 10개씩
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page':page, 'kw':kw}
    return render(request, 'pybo/question_list.html',context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)    