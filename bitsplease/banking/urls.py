from django.conf.urls import url, include
from . import views

urlpatterns = [
    # ex: /banking/
    url(r'^$', views.index, name='index'),
    # ex: /banking/my/
    url(r'^my$', views.my_view, name='my_view'),
    # ex: /banking/account/RO2325236/
    # url(r'^account/(?P<pk>)/$', views.acc_detail, name='acc-detail'),
]