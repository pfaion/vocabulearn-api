from django.http import JsonResponse

from ..auth_tools import auth_only


@auth_only
def test(request):
    return JsonResponse({'data': 42})
