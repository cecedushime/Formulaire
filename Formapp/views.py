
from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Etudiant
from .forms import EtudiantForm
from django.conf import settings
from twilio.rest import Client
from django.http import JsonResponse



class AjouterEtudiant(View):
    def get(self, request):
        form = EtudiantForm()
        return render(request, 'ajouter_etudiant.html')

    def post(self, request):
        
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('Formapp:ajouter_etudiant')  
        return render(request, 'ajouter_etudiant.html', {'form': form})

class ListerEtudiants(View):
    def get(self, request):
        etudiants = Etudiant.objects.all()  
        return render(request, 'lister_etudiants.html', {'etudiants': etudiants})
    
def send_whatsapp_message(to, message):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=message,
        from_=settings.TWILIO_WHATSAPP_NUMBER,
        to=f'whatsapp:{to}'
    )
    return message.sid    

class EnvoyerMessage(View):
    def post(self, request):
        numero = request.POST.get('numero')
        message = request.POST.get('message')

        if numero and message:
            message_sid = send_whatsapp_message(numero, message)
            return JsonResponse({'status': 'success', 'message_sid': message_sid})
        return JsonResponse({'status': 'error', 'message': 'Numéro ou message manquant.'})
    
        
        