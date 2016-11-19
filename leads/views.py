from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse

from .models import Lead
from .forms import LeadForm

def landing_web(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)

        if form.is_valid():
            lead = form.save()
            lead.save()
            return redirect('/gracias')

    else:
        form = LeadForm()

    context = {
        'form': form
    }
    template = loader.get_template('leads.html')

    return HttpResponse(template.render(context, request))
