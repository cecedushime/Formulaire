
from django.views import View
from django.shortcuts import render, redirect
from .forms import EtudiantForm
from django.http import JsonResponse
from firebase_admin import firestore


db = firestore.client()
class AjouterEtudiant(View):
    def get(self, request):
        form = EtudiantForm()  # Assurez-vous que ce formulaire est défini
        return render(request, 'ajouter_etudiant.html', {'form': form})

    def post(self, request):
        if request.method == 'POST':
            nom = request.POST.get('nom')
            prenom = request.POST.get('prenom')
            email = request.POST.get('email')

            # Vérifier si un étudiant avec le même nom et prénom existe déjà
            existing_student = db.collection('contact').where('nom', '==', nom).where('prenom', '==', prenom).limit(1).get()

            if existing_student:
                # Si un étudiant avec le même nom et prénom existe déjà, afficher un message d'erreur
                return render(request, 'ajouter_etudiant.html', {
                    'form': EtudiantForm(),
                    'error': 'Un étudiant avec ce nom et prénom est déjà enregistré.'
                })

            # Sinon, ajoutez l'étudiant
            db.collection('contact').add({
                'nom': nom,
                'prenom': prenom,
                'email': email,
                'date_inscription': firestore.SERVER_TIMESTAMP
            })

            return redirect('Formapp:success_page')  # Redirigez vers la page de succès

        return render(request, 'ajouter_etudiant.html', {'form': form})

def success_page(request):
    return render(request, 'success_page.html') 
   

class ListerEtudiants(View):
    def get(self, request):
        etudiants_ref = db.collection('contact').order_by('date_inscription')
        etudiants = etudiants_ref.stream()

        etudiant_list = [{"id": doc.id, **doc.to_dict()} for doc in etudiants]
        
        return render(request, 'lister_etudiants.html', {'etudiants': etudiant_list})

class EnvoyerMessage(View):
    def post(self, request):
        numero = request.POST.get('numero')
        message = request.POST.get('message')

        if numero and message:
            message_sid = send_whatsapp_message(numero, message)
            return JsonResponse({'status': 'success', 'message_sid': message_sid})
        return JsonResponse({'status': 'error', 'message': 'Numéro ou message manquant.'})
    
    
def afficher_etudiants(request):
    etudiants = db.collection('contact').stream()
    etudiant_list = [{"id": doc.id, **doc.to_dict()} for doc in etudiants]
    return render(request, 'lister_etudiants.html', {'etudiants': etudiant_list})        


