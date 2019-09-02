from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello! It's the dash. Dash index")