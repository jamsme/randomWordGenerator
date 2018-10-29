from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if not 'counter' in request.session:
        request.session['counter'] = 1

    context = {
        'randword' : get_random_string(length=14),
    }
    print(context)
    print(request.session['counter'])
    return render(request, "first_app/index.html", context)

def random(request):
    request.session['counter'] += 1
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')

# Create your views here.
