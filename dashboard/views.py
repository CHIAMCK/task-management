from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.template import loader
from django.http import HttpResponse


class MainDashboardView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        company_content = {

        }
        template_loader = loader.get_template('dashboard_company.html')
        response = HttpResponse(template_loader.render(company_content, request))

        return response
