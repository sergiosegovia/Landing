from django.utils.translation import ugettext_lazy as _
from django import forms

from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'
        labels = {
            'name': _('Nombre'),
            'email': _('Email'),
            'phone': _('Telefono'),
            'ads': _('Acepta recibir promociones a su email'),
        }
