from django.shortcuts import render
from django.views.generic import ListView
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
#import forms

from challangeapp.models import user_list

class ListContactView(ListView):

    model = user_list
    template_name = 'contact_list.html'

class CreateContactView(CreateView):

    model = user_list
    template_name = 'edit_contact.html'
    #form_class = forms.ContactForm

    def get_success_url(self):
        return reverse('contacts-list') 
    def get_context_data(self, **kwargs):
        context = super(CreateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-new')
        return context
class UpdateContactView(UpdateView):

    model = user_list
    template_name = 'edit_contact.html'
    #form_class = forms.ContactForm

    def get_success_url(self):
        return reverse('contacts-list')
    def get_context_data(self, **kwargs):
        context = super(UpdateContactView, self).get_context_data(**kwargs)
        context['action'] = reverse('contacts-edit', kwargs={'pk': self.get_object().id})
        return context
        
class DeleteContactView(DeleteView):

    model = user_list
    template_name = 'delete_contact.html'

    def get_success_url(self):
        return reverse('contacts-list')
        
class ContactView(DetailView):

    model = user_list
    template_name = 'contact.html'