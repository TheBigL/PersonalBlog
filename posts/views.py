from django.http import HttpResponse
from django.views.generic import TemplateView
from django.template import loader
# Create your views here.
def HomeView (TemplateView):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())