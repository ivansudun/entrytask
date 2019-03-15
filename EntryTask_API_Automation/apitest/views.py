# -*- coding: utf-8 -*-
from django.http import HttpResponse,JsonResponse
from django.views.decorators.http import require_http_methods

from settings import *

# Create your views here.
@require_http_methods(["GET"])
def test(request):
    #进行阐述合法性检查
    try:
        a = int( request.GET.get( "a" , "" ) )
    except ValueError:
        return JsonResponse( return_json( PARAMS_ERRCODE ) , safe = False )
    except:
        return JsonResponse( return_json( SYSTEM_ERRCODE ) , safe = False )
        
    b = request.GET.get( "b" , "" )
    if not b:
        return JsonResponse( return_json( PARAMS_ERRCODE ) , safe = False )
    
    return JsonResponse(dict({ "reference" : "NO.%d is %s" % ( a, b ) }, **return_json( SUCCESS_CODE ) ) , safe = False )
