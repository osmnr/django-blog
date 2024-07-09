from django.utils.deprecation import MiddlewareMixin
from .models import Log
import time
from datetime import datetime, timedelta

class LoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        self.start_time = time.time()
        self.log_entry = Log(
            path = request.path,
            method = request.method,
            requestHeaders = self.serialize_headers(request.headers),
            senderIP = request.META.get('REMOTE_ADDR'),
            userAgent = request.META.get('HTTP_USER_AGENT')
            )
        if request.GET:
            self.log_entry.getParams = self.serialize_params(request.GET)
        if request.method == 'POST':
            self.log_entry.postData = self.serialize_params(request.POST)
        print("this is self.log_entry value: ",self.log_entry)

    def process_response(self, request, response):
        self.log_entry.statusCode = response.status_code
        self.log_entry.responseHeaders = self.serialize_headers(response.headers)
        self.log_entry.responseContent = response.content.decode('utf-8')[0:1024]
        self.log_entry.responseTime = self.calculate_response_time()
        self.log_entry.save()
        print("this is self.log_entry value: ",self.log_entry)
        return response
    
    def serialize_headers(self, headers):
        return '\n'.join(f'{key}:{value}' for key, value in headers.items())
    
    def serialize_params(self, params):
        return '\n'.join(f'{key}:{value}' for key, value in params.items())

    def calculate_response_time(self):
        return time.time()-self.start_time

    now = datetime.now()
    print("this is nowwww:", now)
    if(now.hour== 19):
        oldThanXmonths = datetime.now() - timedelta(minutes=5)
        x = Log.objects.filter(createdAt__lte = oldThanXmonths).delete()

             

    
    