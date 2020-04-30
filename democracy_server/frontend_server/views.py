from django.shortcuts import render
from threads.models import ThreadModel, ReplyModel
from django.db.models import Q


def catalog_view(request):
    # get recent threads set
    catalog_threads = ThreadModel.objects.all().order_by("time_posted")
    context = {"catalog_threads": catalog_threads}
    return render(request, "catalog.html", context)


def view_thread(request, id):
    thread = ThreadModel.objects.get(pk=id)
    replies_with_thread = ReplyModel.objects.filter(
        Q(thread=thread) & Q(with_thread=True)
    )
    replies_against_thread = ReplyModel.objects.filter(
        Q(thread=thread) & Q(with_thread=False)
    )
    context = {
        "thread": thread,
        "replies_with": replies_with_thread,
        "replies_against": replies_against_thread,
    }
    return render(request, "thread.html", context)


def create_thread(request):
    if request.method == "GET":
        # show the create new thread form
        pass
    elif request.method == "POST":
        # handle a thread POST operation and redirect
        pass
    else:
        # return invalid method
        pass
