from django.http import HttpResponse
from django.template import loader
# Create your views here.
def posts (request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())