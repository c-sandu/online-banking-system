from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic

from .models import User, Account, Transaction

# Create your views here.

class AccDetailView(generic.DetailView):
    model = Account

def customer_view(request):
    user = request.user
    accounts = Account.objects.filter(owner__username=user)
    context = {'accounts': accounts}
    return render(request, 'banking/client.html', context)

def banker_view(request):
    context = {}
    return render(request, 'banking/banker.html', context)



#@login_required
def my_view(request):
    user = request.user
    if user.user_type == user.CUSTOMER:
        return customer_view(request)
    elif user.user_type == user.BANKER:
        return banker_view(request)
    return customer_view(request)

def index(request):
    """
    View function for home page
    """
    #TODO: ceva aici
    context = {}
    return render(request, 'banking/index.html', context)
