from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# remember to fix this later
@csrf_exempt
def index(request):
    return render(request, "fileupload/index.html")


@csrf_exempt
def browser(request):
    return render(request, 'fileupload/browser.html')
