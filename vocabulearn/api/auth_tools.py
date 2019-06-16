from django.http import JsonResponse, HttpResponse, Http404
from django.conf import settings
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

import jwt
from pprint import pprint

def token(request):
    if request.method == 'POST':
        if 'username' not in request.POST or 'password' not in request.POST:
            return HttpResponse('Error: Authentication data not found in POST data.', status=400)

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse('Error: Username and/or password were incorrect!', status=401)

        payload = dict(username=username, password=password)
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
        return JsonResponse({'token': token})

    if request.method == 'GET' and settings.DEBUG:
        if 'username' not in request.GET or 'password' not in request.GET:
            return HttpResponse('Error: Authentication data not found in GET data.', status=400)

        username = request.GET['username']
        password = request.GET['password']
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse('Error: Username and/or password were incorrect!', status=401)
 
        payload = dict(username=username, password=password)
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
        return JsonResponse({'token': token})

    raise Http404('Method not handled.')


def auth_only(func):
    def wrapper(request, *args):
        key = 'HTTP_AUTHTOKEN'
        pprint(request.META)
        if key not in request.META:
            return HttpResponse('Error: No authentication token present!', status=401)
        token = request.META[key]
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        username = payload['username']
        password = payload['password']
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse('Error: Username and/or password were incorrect!', status=401)
        return func(request, *args)
    return csrf_exempt(wrapper)
