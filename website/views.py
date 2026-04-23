from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from .forms import AppointmentForm
from .models import Appointment

def home(request):
    message = None
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            # Return "OK" as plain text for AJAX requests
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return HttpResponse('OK')
            # Redirect to confirmation page for regular form submission
            return redirect('appointment_confirmation', appointment_id=appointment.id)
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'status': 'error', 'errors': form.errors})
            message = 'There was an error booking your appointment.'
    else:
        form = AppointmentForm()
    return render(request, 'index.html', {'form': form, 'message': message})

def appointment_confirmation(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    return render(request, 'confirmation.html', {'appointment': appointment})

def service_detail(request):
    return render(request, 'service-details.html')

def starter(request):
    return render(request, 'starter-page.html')
