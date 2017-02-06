from django.shortcuts import render
from .models import TestModel
# Create your views here.


def test_list(request):
    qs = TestModel.objects.all()

    context = {
        "objects": qs,
    }
    template = 'tests_list_view.html'
    return render(request, template, context)