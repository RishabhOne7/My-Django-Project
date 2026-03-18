class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        from .models import VisitorLog

        if not request.path.startswith('/admin'):
            ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', ''))
            if ',' in ip:
                ip = ip.split(',')[0].strip()

            browser = request.META.get('HTTP_USER_AGENT', '')[:200]

            VisitorLog.objects.create(
                ip_address=ip or '0.0.0.0',
                page_visited=request.path,
                browser=browser,
            )

        return self.get_response(request)