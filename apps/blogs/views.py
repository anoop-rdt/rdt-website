from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.contrib.admin.views.decorators import staff_member_required

from models import Blog
from django.conf.urls import patterns
from django.contrib import admin
from django.http import HttpResponse
from endless_pagination.views import AjaxListView    


class BlogListView(AjaxListView):

    model = Blog
    
    context_object_name = 'blogs'
    page_template = 'blog_listing_template.html'
    paginate_by = 3


class BlogDetailView(DetailView):

    model = Blog

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        return context