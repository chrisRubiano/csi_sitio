from django.conf.urls import include, url
from . import views

urlpatterns = [
		url(r'^$', views.index, name='index'),
        url(r'^blog/$', views.post_list),                            #URL para lista de todos los post
        url(r'^blog/post/(?P<pk>[0-9]+)/$', views.post_detail),      #URL para ver los detalles del post
        url(r'^blog/post/new/$', views.post_new, name='post_new'),   #URL para crear un nuevo post sin el panel de admin
        url(r'^blog/post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'), #URL para editar los post sin el panel de admin
    ]
