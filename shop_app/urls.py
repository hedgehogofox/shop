from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='product_list'),
    url(r'^search/$', views.search, name='search_results'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list,
        name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',
        views.product_detail,
        name='product_detail'),
    
]
