from django.shortcuts import render
from django.http import HttpResponse

from threads.models import ThreadModel

def stub_view(request):
    pass


def thread_count(request):
    thread_count = ThreadModel.objects.all().count()
    return HttpResponse(thread_count)
