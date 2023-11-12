from django.http import HttpRequest, HttpResponse
from django.views import View


class MainView(View):
    """Main view for schedule"""

    def get(self, request: HttpRequest):
        """Get method"""
        return HttpResponse('ok')
