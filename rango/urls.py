from django.conf.urls import  url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),    
    url(r'^objects/', views.objects, name = 'objects_main'),
    url(r'^new/$', views.object_new, name='objects_new'),
    url(r'^edit/(\d+)/$', views.edit, name = 'edit'),
    url(r'^del/(\d+)/$', views.delete, name = 'delete'),
]
