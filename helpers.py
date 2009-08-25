from django.http import HttpResponse
from django.utils import simplejson
from django.utils.translation import ugettext as _

from traceback import print_exc

def json_response(func):#{{{
    def inner_func(request, *args, **kwargs):
        try:
            response = func(request, *args, **kwargs)
            if isinstance(response, tuple) and len(response) == 2:
                (type, value) = response
                return HttpResponse(create_response(0, type, value), mimetype="application/json")
            else:
                return response
        except Exception, e:
            print_exc()
            if hasattr(e, "message"):
                msg = e.message
            else:
                msg = _(u"Internal Error") + ": " + str(e)
                response = create_response(500, "string", msg)

    inner_func.__name__ = func.__name__
    inner_func.__dict__ = func.__dict__

    return inner_func#}}}

def create_response(code, type=None, value=None):#{{{
    if type == None and value == None:
        response = {
                        "code": code,
                        "data": None
                   }
    else:
        response = { 
                        "code": code,
                        "data": {
                            "type": type,
                            "body": value
                            }
                   }

    return simplejson.dumps(response)#}}}

