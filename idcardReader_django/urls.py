from django.contrib import admin
from django.urls import path
from idReader.views import index
from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from idReader import views

urlpatterns = [
    url(r'^favicon.ico$', RedirectView.as_view(url=r'static/ico.ico')),
    path('admin/', admin.site.urls),
    path('', index),
    path('index/', index),
    path('print_test/', views.print_test),
]

