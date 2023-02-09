from django.shortcuts import render


# Create your views here.
def index(request):
    # TODO: add functionality Home page.

    context = {}
    return render(request, 'main/index.html', context=context)
