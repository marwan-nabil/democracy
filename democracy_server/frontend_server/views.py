from django.shortcuts import render
from threads.models import ThreadModel
from django.db.models import prefetch_related_objects


def catalog_view(request):
    # get recent threads set
    catalog_threads = ThreadModel.objects.all().order_by("time_posted")
    context = {"catalog_threads": catalog_threads}
    return render(request, "frontend_server/catalog.html", context)


def view_thread(request, id):
    pass


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
