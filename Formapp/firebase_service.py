from firebase_admin import firestore

# Créer une référence à Firestore
db = firestore.client()

def ajouter_etudiant(nom, email):
    # Ajouter un nouvel étudiant à la collection 'etudiants'
    db.collection('etudiants').add({
        'nom': nom,
        'email': email
    })

def lister_etudiants():
    # Récupérer tous les étudiants
    etudiants = []
    docs = db.collection('etudiants').stream()

    for doc in docs:
        etudiants.append(doc.to_dict())
    
    return etudiants