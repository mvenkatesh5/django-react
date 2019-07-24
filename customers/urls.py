from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/customers/$', views.CustomersList.as_view()),
    url(r'^api/customers/(?P<pk>[0-9]+)$', views.CustomersDetails.as_view()),
]