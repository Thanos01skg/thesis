from django.contrib import admin  # Η διαχειριστική διεπαφή επιτρέπει στους χρήστες με δικαιώματα διαχειριστή να βλέπουν, να διαχειρίζονται, και να τροποποιούν δεδομένα που αποθηκεύονται στην βάση δεδομένων
from .models import Device, Signal  # Εισαγωγή μοντέλων Device και Signal από το αρχείο models.py της εφαρμογής


admin.site.register(Device)  # Εγγραφή μοντέλου Device στο Django Admin
admin.site.register(Signal)  # Εγγραφή μοντέλου Signal στο Django Admin