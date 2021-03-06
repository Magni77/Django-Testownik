from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .form import TestForm, QuestionForm, AnswerForm,  UploadFileForm
from .models import TestModel, AnswerModel, QuestionModel
from .upload_handler import UploadHandler


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            files = request.FILES.getlist('file')
            UploadHandler(request, files, form)
            return HttpResponseRedirect('/upload')
    else:
        form = UploadFileForm()
    return render(request, 'create_view.html', {'form': form})


class TestCreate(CreateView):
    model = TestModel
    template_name = 'create_view.html'
    fields = ['title', 'user']


class QuestionCreate(CreateView):
    model = QuestionModel
    template_name = 'create_view.html'
    fields = ['question', 'hint', 'test', ]

    def get_form(self, form_class=None):
        return QuestionForm


class AnswerCreate(CreateView):
    model = AnswerModel
    template_name = 'create_view.html'
    fields = ['answer', 'img_answer', 'is_correct', 'question', 'user' ]

    def get_form(self, form_class=None):
        return AnswerForm


class TestListView(ListView):
    model = TestModel
    template_name = 'test_detail.html'


def test_list(request):
    qs = TestModel.objects.all()
    ans = AnswerModel.objects.all()
    context = {
        "objects": qs,
        "answers": ans
    }
    template = 'tests_list_view.html'
    return render(request, template, context)


# def task_create(request):
#     form = TestForm(request.POST or None)
#     context = {
#         "form": TestForm
#     }
#     if form.is_valid():
#         obj = form.save(commit=False)
#         obj.save()
#         context = {
#             'form': TestForm()
#         }
#
#     template = 'create_view.html'
#     return render(request, template, context)


