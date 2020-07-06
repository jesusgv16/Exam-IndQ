from django import forms
from .models import Event
from django import forms
from django.contrib.auth.models import User

from .models import Event
class DateInput(forms.DateInput):
	input_type='date'

class EventForm(forms.ModelForm):
	date = forms.DateField(widget=DateInput)
	class Meta:
		model = Event
		fields = ['title', 'description', 'date','WillYouAttend', 'longitud', 'latitud' ]	    