"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # Εισάγει τη μονάδα διαχειριστή Django, η οποία παρέχει τη διεπαφή διαχειριστή για τη διαχείριση του έργου Django.
from django.urls import path,include # Εισάγει path για τον καθορισμό μοτίβων URL και περιλαμβάνει για τη συμπερίληψη άλλων διαμορφώσεων URL από εφαρμογές.
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_tools_stats/', include('admin_tools_stats.urls')),
    path('temperature-chart/', views.temperature_chart, name='temperature_chart'),  # Direct path to the chart
    path('api/temperature/', views.get_temperature_data, name='temperature_data'),  # Direct path to the API
    path('myapp/', include('myapp.urls')),
    path('api/', include('myapp.urls')), # Περιλαμβάνει το ίδιο σύνολο μοτίβων URL από τη λειτουργική μονάδα myapp.urls κάτω από το πρόθεμα api/.
    # Αυτό είναι χρήσιμο εάν η εφαρμογή myapp ορίζει τελικά σημεία API χρησιμοποιώντας το Django REST Framework και θέλετε να είναι προσβάσιμα με το πρόθεμα /api/.
]
