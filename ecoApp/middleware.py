import time

from django.utils.deprecation import MiddlewareMixin

from ecoApp.models import CustomerTraffic


class TrafficMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):
        if request.user.is_authenticated:
            duration = time.time() - request.start_time
            # Log page visit
            CustomerTraffic.objects.create(
                user=request.user,
                path=request.path,
                duration=duration
            )
        return response