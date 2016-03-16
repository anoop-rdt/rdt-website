from django.views import generic
from forms import ContactForm
from django.template import loader
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage


class HomePage(generic.TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['home_page'] = True
        return context


class ContactUsPage(generic.TemplateView):
    template_name = "contact-us.html"

    def get_context_data(self, **kwargs):
        context = super(ContactUsPage, self).get_context_data(**kwargs)
        contact_form = ContactForm(self.request.POST or None)
        context["contact_form"] = contact_form
        return context


class PythonDjangoPage(generic.TemplateView):
    template_name = "python-django.html"


class JavascriptPage(generic.TemplateView):
    template_name = "javascript.html"


class CrossPlatformPage(generic.TemplateView):
    template_name = "cross-platform.html"


class CustomerSuccessPage(generic.TemplateView):
    template_name = "customer_success.html"


class WhoweServePage(generic.TemplateView):
    template_name = "whoweserve.html"


def customer_contact(request):
    contact_form = ContactForm(request.POST)
    if contact_form.is_valid():
        c = Context({'contact_name': contact_form.cleaned_data['contact_name'],
                    'contact_email': contact_form.cleaned_data['contact_email'],
                    'contact_phone': contact_form.cleaned_data['contact_phone'],
                    'content' : contact_form.cleaned_data['content']
            })
        message = get_template('contact_email.html').render(c)
        msg = EmailMessage(contact_form.cleaned_data['subject'], message, to=[settings.CONTACT_EMAIL], from_email=contact_form.cleaned_data['contact_email'])
        msg.content_subtype = 'html'
        msg.send()
        response = HttpResponse("Thank you for contacting us.We will get back to you at the earliest.")
    else:
        response = HttpResponse("Some error occured.")
        return response