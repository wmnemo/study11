from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),  #localhost:8000/post/1
    #url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/new/$', views.post_new_form, name='post_new'),
]