from django.db import models

# Δημιουργεί ένα νέο μοντέλο (πίνακα στη βάση δεδομένων)
class Device(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    id = models.BigAutoField(primary_key=True)

    def __str__(self):  # Καθορίζει την εμφάνιση του αντικειμένου όταν το βλέπουμε στο Django Admin
        return self.name  # Επιστρέφει το όνομα της συσκευής (self.name), που σημαίνει ότι όταν βλέπουμε μια συσκευή, θα εμφανίζεται με το όνομά της


# Δημιουργεί ένα νέο μοντέλο (πίνακα στη βάση δεδομένων) που θα αποθηκεύει πληροφορίες για τα σήματα και Signal είναι το όνομα της κλάσης (δηλαδή ο πίνακας)   
class Signal(models.Model):  
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    # Δημιουργεί μια στήλη στη βάση δεδομένων συνδέοντας το Signal με μια εγγραφή του μοντέλου Device. 
    # Το ForeignKey ορίζει μια σχέση "πολλά προς ένα", δηλαδή κάθε σήμα σχετίζεται με μία συσκευή, 
    # αλλά μία συσκευή μπορεί να έχει πολλά σήματα. Το on_delete=models.CASCADE σημαίνει ότι αν η συσκευή διαγραφεί, 
    # τότε όλα τα σήματα που σχετίζονται με αυτήν θα διαγραφούν επίσης.
    timestamp = models.DateTimeField(auto_now_add=True) # Αποθήκευση ημερομηνίας ώρας κατά τη δημιουργία του σήματος και η χρονική σήμανση ορίζεται αυτόματα όταν δημιουργείται το αντικείμενο Signal
    value = models.FloatField()  # Αποθήκευση τιμής σήματος (π.χ. τιμή μιας μέτρησης)
    signal_type = models.CharField(max_length=50) # Αποθήκευση τύπο σήματος (π.χ. θερμοκρασία, υγρασία, πίεση κλπ)
    id = models.BigAutoField(primary_key=True)


def __str__(self):   # Καθορίζει την εμφάνιση του αντικειμένου όταν το βλέπουμε στο Django Admin
    return f"{self.device.name} - {self.signal_type} - {self.timestamp}" 
    # Δημιουργεί και επιστρέφει μια συμβολοσειρά που περιέχει το όνομα της συσκευής, τον τύπο του σήματος και τη 
    # χρονική σήμανση, βλέποντας τα δεδομένα του σήματος σε ευανάγνωστη μορφή, π.χ., όταν το βλέπετε στη Django Admin.