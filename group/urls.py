from django.conf.urls import url, include
import xadmin

from apps.index import views

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('account/', include('apps.account.urls')),
    url('^$', views.index, name='index'),
    url('detail/', include('apps.detail.urls')),
    url('car/', include('apps.car.urls')),
    url('order/', include('apps.order.urls')),
    url('search/', include('apps.search.urls')),
]
