from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.BlogListView.as_view(), name="blog_list"),
    url(r'^(?P<slug>[-\w]+)', views.BlogDetailView.as_view(), name='blog_detail'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
