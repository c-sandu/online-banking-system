from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import User, Account, Transaction

# Create your views here.

def acc_detail(request, acc_iban):
    account = get_object_or_404(Account, iban=acc_iban)
    return render(request, 'banking/account_detail.html', {'account': account})

def user_detail(request, username):
    # user = get_object_or_404(User, username=username)
    accounts = Account.objects.filter(owner__username=username)
    context = {'accounts': accounts}
    return render(request, 'banking/client.html', context)

def customer_view(request):
    user = request.user
    accounts = Account.objects.filter(owner__username=user)
    context = {'accounts': accounts}
    return render(request, 'banking/client.html', context)

def banker_view(request):
    users = User.objects.filter(Q(user_type=User.CUSTOMER) | Q(user_type=User.VENDOR))
    print(users)
    context = {'users': users}
    return render(request, 'banking/banker.html', context)


"""def login(request):
    context = {}
    context.update(csrf(request))
    return render(request, 'banking/login.html', context)"""

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    auth_code = request.POST.get('auth_code', '')

    user = auth.authenticate(username=username, password=password, auth_code=auth_code)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/login')
    else:
        return None




@login_required
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
