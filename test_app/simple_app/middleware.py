from django.utils import timezone
from django.http import HttpRequest, HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings


class LogAllRequestsMiddleware(MiddlewareMixin):
    ''' Middleware fir logging all requests wtih params '''

    def process_response(self, request: HttpRequest, response: HttpResponse) -> HttpResponse:
        ''' logging all request to file'''
        params: dict = self._get_params(request)
        loger_dict: dict = {
            'time': timezone.now(),
            'url': request.path,
            'method': request.method,
            'status': response.status_code,
            'params': params,
        }
        with open(settings.LOG_FILE, 'a') as file:
            file.write(f'{loger_dict}\n')

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
