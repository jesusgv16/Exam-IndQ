from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, get_user_model,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

from .forms import EventForm 
from .models import Event

# Create your views here.
@login_required
def events_view(request):
	if request.method == 'POST':
		events_form = EventForm(data=request.POST)
		if events_form.is_valid():
			print('valido')
			events_form.save()
			return redirect('home')
	else:

		events_form = EventForm()
	return render(request, 'events.html', {'events_form': events_form})	

@login_required
def listEvents_view(request):

	eventos =  Event.objects.all()
	return render(request, 'levents.html', {'eventos': eventos})       


