from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Sum
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic

from dash.models import Client, Order


# Create your views here.
def index(request):
    return render(request, 'dash/index.html')


class ClientDetail(generic.DetailView):
    model = Client
    template_name = 'dash/client.html'


class ClientList(generic.ListView):
    template_name = 'dash/client_list.html'
    context_object_name = 'client_list'

    def get_queryset(self):
        return Client.objects.all()


class ClientCreate(generic.CreateView):
    model = Client
    template_name= "dash/object_new.html"
    fields = [
        'name',
        'surname',
        'birthdate',
        'email',]

class OrderCreate(generic.CreateView):
    model = Order
    template_name = "dash/object_new.html"
    fields = [
        'client',
        'comment',
        'parameters',