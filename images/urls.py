from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=(
    re_path('^$',views.welcome,name = 'welcome'),
    re_path('^search/', views.search_results, name='search_results'),
)