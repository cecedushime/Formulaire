from django.db import models
from firebase_admin import firestore
from datetime import datetime


db = firestore.client()

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_inscription = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} ({self.email})"

    def save_to_firestore(self):
        
        doc_ref = db.collection('contact').add({
            'nom': self.nom,
            'prenom': self.prenom,
            'email': self.email,
            'date_inscription': self.date_inscription
        })
        return doc_ref.id  


