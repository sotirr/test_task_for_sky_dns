from django.utils import timezone
from django.http import HttpRequest, HttpResponse
from django.utils.deprecation import MiddlewareMixin

import logging

logger = logging.getLogger('request_to_file')


class LogAllRequestsMiddleware(MiddlewareMixin):
    ''' Middleware fir logging all requests with params '''

    def process_response(self, request: HttpRequest, response: HttpResponse) -> HttpResponse:
        ''' logging all request to file'''
        params: dict = self._get_params(request)
        logger_dict: dict = {
            'time': timezone.now(),
            'url': request.path,
            'method': request.method,
            'status': response.status_code,
            'params': params,
        }

        logger.info(f'{logger_dict}')
        return response

    def _get_params(self, request: HttpRequest) -> dict:
        ''' collect important request params '''
        params: dict = {}
        if request.GET:
            params.update(request.GET.dict())
        if request.POST:
            params.update(request.POST.dict())
        params.pop('csrfmiddlewaretoken', None)
        return params
