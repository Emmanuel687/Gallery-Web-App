from django.urls import re_path
from django.conf import settings
from . import views

urlpatterns=(
    re_path('^$',views.welcome,name = 'welcome'),
)