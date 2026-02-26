# Εισαγωγή κλάσης AppConfig (υπεύθυνη για τη διαμόρφωση των εφαρμογών ενός Django έργου) από το module django.apps
from django.apps import AppConfig  

# Δημιουργία κλάσης που διαχειρίζεται τη διαμόρφωση της εφαρμογής myapp
class MyappConfig(AppConfig):
    name = 'myapp'  # Όνομα εφαρμογής στο Django project
