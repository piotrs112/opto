from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.db.models import Sum
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from dash.models import Client, Order
from accounts.models import Employee


# Create your views here.
def index(request):
    return render(request, 'dash/index.html')


class ClientDetail(generic.DetailView, LoginRequiredMixin):
    model = Client
    template_name = 'dash/client.html'
    
    def get_queryset(self):
        self.clients = get_object_or_404(Client)
        return Client.objects.filter(clientOf=self.request.user.employee.employer)


class ClientList(generic.ListView, LoginRequiredMixin):
    template_name = 'dash/client_list.html'
    context_object_name = 'client_list'

    def get_queryset(self):
        self.clients = get_list_or_404(Client)
        return Client.objects.filter(clientOf=self.request.user.employee.employer)


class ClientCreate(generic.CreateView, LoginRequiredMixin):
    model = Client
    template_name= "dash/object_new.html"
    fields = [
        'name',
        'surname',
        'birthdate',
        'email',
    ]
    
    
    def form_valid(self, form):
        form.instance.clientOf = self.request.user.employee.employer

        return super().form_valid(form)


class OrderCreate(generic.CreateView, LoginRequiredMixin):
    model = Order
    template_name = "dash/object_new.html"
    fields = [
        'client',
        'comment',
        'parameters',
    ]

    def form_valid(self, form):
        form.instance.clientOf = self.request.user.employee.employer

        return super().form_valid(form)

class OrderDetail(generic.DetailView, LoginRequiredMixin):
    model = Order
    template_name = 'dash/order.html'


class OrderList(generic.ListView, LoginRequiredMixin):
    template_name = 'dash/order_list.html'
    context_object_name = 'client_list'

    def get_queryset(self):
        return Order.objects.all()