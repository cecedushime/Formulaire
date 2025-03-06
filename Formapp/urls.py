from django.urls import path
from .views import AjouterEtudiant, ListerEtudiants, EnvoyerMessage, success_page

app_name = "Formapp"
urlpatterns = [
    
    path('',AjouterEtudiant.as_view(), name='ajouter_etudiant'), 
    path('success/', success_page, name='success_page'),
    path('lister/', ListerEtudiants.as_view(), name='lister_etudiants'), 
    path('envoyer-message/', EnvoyerMessage.as_view(), name='envoyer_message'),
     
]