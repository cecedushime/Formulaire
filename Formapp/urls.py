from django.urls import path
from .views import AjouterEtudiant, ListerEtudiants, EnvoyerMessage 

app_name = "Formapp"
urlpatterns = [
    
    path('',AjouterEtudiant.as_view(), name='ajouter_etudiant'), 
    path('lister/', ListerEtudiants.as_view(), name='lister_etudiants'), 
     path('envoyer-message/', EnvoyerMessage.as_view(), name='envoyer_message'),
     
]