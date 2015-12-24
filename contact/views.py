__author__ = 'trigger'

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from contact.forms import ContactForm


def contact(request):
    global form
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
             cd = form.cleaned_data
             send_mail(
               cd['subject'],
               cd['message'],
               cd.get('e-mail', 'noreply@example.com'),
               ['siteowner@example.com' ],
                      )
             return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': 'I like Yor`s site '}
        )

    return render(request, 'contact_form.html', {'form': form})

