from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.post_list, name='index'),
    url(r'^me/$', views.me, name='me'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls'))
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
