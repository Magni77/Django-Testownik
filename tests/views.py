from django.shortcuts import render, HttpResponseRedirect
from .models import TestModel, AnswerModel, QuestionModel
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from .form import TestForm, QuestionForm, AnswerForm,  UploadFileForm
from .upload_handler import handle_uploaded_file


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            test_choice = form.cleaned_data.get('test_choice')
          #  handle_uploaded_file(request.FILES['file'])
            files = request.FILES.getlist('file')
            print(request.FILES.getlist('file'))
            for f in files:
                handle_uploaded_file(f, test_choice)
            return HttpResponseRedirect('/testownik/upload')
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


def task_create(request):
    form = TestForm(request.POST or None)
    context = {
        "form": TestForm
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        context = {
            'form': TestForm()
        }

    template = 'create_view.html'
    return render(request, template, context)