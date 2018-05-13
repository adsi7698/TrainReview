from django import forms
from . import models
from django.template import RequestContext

class PassengerReview(forms.ModelForm):
    class Meta:
        model = models.PassengerReview
        fields = ['trainName', 'title', 'body', 'doc_image']