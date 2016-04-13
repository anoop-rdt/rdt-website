from django import forms
from django.contrib import admin
from djangoseo.admin import register_seo_admin
from seo import RawdataMetadata

from ckeditor.widgets import CKEditorWidget

from models import Blog, Category



class BlogAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())
    
    class Meta:
    	model = Blog
        exclude = ['posted']


class BlogAdmin(admin.ModelAdmin):
	form = BlogAdminForm
	exclude = ['posted']
	prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
register_seo_admin(admin.site, RawdataMetadata)
