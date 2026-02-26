from django.urls import path,include  # Εισαγωγή συνάρτησης path που χρησιμοποιείται για να συνδέσουμε URLs με views (URL patterns)
from rest_framework.routers import DefaultRouter  # Εισαγωγή του DefaultRouter από το Django REST Framework, όπου είναι ένα αυτόματο router που επιτρέπει να ορίσουμε API endpoints για ViewSets χωρίς να χρειάζεται να δημιουργούμε χειροκίνητα URLs για αυτά
from .views import DeviceViewSet, SignalViewSet, signals_view   # Εισαγωγή τριών views από το τοπικό αρχείο views.py
# Ένα ViewSet που σχετίζεται με το μοντέλο Device και διαχειρίζεται τα API endpoints για τις συσκευές
# Ένα ViewSet που σχετίζεται με το μοντέλο Signal και διαχειρίζεται τα API endpoints για τα σήματα
# Ένα custom view που δημιουργεί μια ειδική προβολή για τα σήματα, π.χ., στον Django Admin
from . import views


router = DefaultRouter()  # Δημιουργία νέου router, που αναλαμβάνει να δημιουργήσει αυτόματα τα URLs για τα API endpoints με βάση τα ViewSets που θα του καταχωρήσουμε
router.register(r'devices', DeviceViewSet)  #
router.register(r'signals', SignalViewSet)  #

# 
urlpatterns = [
    path('', include(router.urls)),  #
    path('admin/myapp/signals/', signals_view, name='signals_view'),  #
    path('api/temperature/', views.get_temperature_data, name='temperature_data'),
    path('temperature-chart/', views.temperature_chart, name='temperature_chart'),
]