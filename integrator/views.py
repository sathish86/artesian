from django.shortcuts import render, redirect
from integrator.forms import RegistrationForm

# Create your views here.


def home(request):
    return render(request, 'integrator/home.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/integrator')
        else:
            context = {'form': form}
            return render(request, 'integrator/registration_form.html', context)
    else:
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'integrator/registration_form.html', context)
