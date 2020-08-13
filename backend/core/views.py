import functools
import logging
import traceback

from django.conf import settings
from django.db import transaction
from django.http import JsonResponse
from django.views import View

logger = logging.getLogger(__name__)

JSON_DUMPS_PARAMS = {
    'ensure_ascii': False
}


def ret(json_object, status=200):
    """Returns JSON with valid HTTP headers and readable cyrillic symbols"""
    return JsonResponse(
        json_object,
        status=status,
        safe=not isinstance(json_object, list),
        json_dumps_params=JSON_DUMPS_PARAMS
    )


def error_response(exception):
    """Returns formatted HTTP response error"""
    response = {'errorMessage': str(exception)}
    if settings.DEBUG:
        response['traceback'] = traceback.format_exc()
    return ret(response, status=400)


def base_view(func):
    """Decorator that handles exceptions"""

    @functools.wraps(func)
    def inner(request, *args, **kwargs):
        try:
            with transaction.atomic():
                return func(request, *args, **kwargs)
        except Exception as e:
            logger.error(str(e))
            return error_response(e)

    return inner


class BaseView(View):
    """Base class that handles exceptions and make additional actions"""
    redirect_authenticated = False

    def dispatch(self, request, *args, **kwargs):
        try:
            response = super().dispatch(request, *args, **kwargs)
        except Exception as e:
            logger.error(str(e))
            return self._response({'errorMessage': str(e)}, status=400)

        if isinstance(response, (dict, list)):
            return self._response(response)
        else:
            return response

    @staticmethod
    def _response(data, *, status=200):
        return JsonResponse(
            data,
            status=status,
            safe=not isinstance(data, list),
            json_dumps_params=JSON_DUMPS_PARAMS
        )
