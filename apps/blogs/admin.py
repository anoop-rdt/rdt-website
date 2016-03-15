from django.contrib import admin
from django import forms

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
