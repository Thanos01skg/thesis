from rest_framework import serializers  # Περιλαμβάνει τις εργαλειοθήκες που επιτρέπουν να μετατρέψουμε τα μοντέλα σε JSON ή άλλες μορφές δεδομένων για τα API
from .models import Device, Signal  # Εισαγωγή μοντέλων Device και Signal από το τοπικό αρχείο models.py

# Δημιουργεί serializer που βασίζεται στο μοντέλο Device
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:  # Καθορίσουμε τις παραμέτρους του serializer, δηλαδή το μοντέλο - τα πεδία που θέλουμε να συμπεριλάβουμε
        model = Device  # Ο serializer αυτός βασίζεται στο μοντέλο Device
        fields = ['id', 'name', 'description']  # Καθορίζει τα πεδία από το μοντέλο Device που θα συμπεριληφθούν στο API

# Δημιουργεί έναν serializer που βασίζεται στο μοντέλο Signal
class SignalSerializer(serializers.ModelSerializer):
    class Meta:  # Χρησιμοποιείται για να καθορίσουμε τις παραμέτρους του serializer, δηλαδή το μοντέλο και τα πεδία που θέλουμε να συμπεριλάβουμε
        model = Signal  # Ο serializer αυτός βασίζεται στο μοντέλο Signal
        fields = ['id', 'device', 'timestamp', 'value', 'signal_type'] # Καθορίζει τα πεδία από το μοντέλο Device που θα συμπεριληφθούν στο API