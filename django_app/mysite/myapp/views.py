# myapp/views.py
from rest_framework import viewsets # Module from Django REST Framework, which simplifies the creation of API views.
from django.shortcuts import render  # Imports the render function, which is used to render HTML templates with context data.
from django.core.serializers.json import DjangoJSONEncoder # Imports a JSON encoder that can handle Django's data types.
from .models import Signal,Device # Imports the Signal and Device models from the current app (myapp).
from .serializers import DeviceSerializer,SignalSerializer # Imports the serializers for Device and Signal, which are used to convert model instances to JSON and vice versa.
from django.http import JsonResponse
from django.utils import timezone
import json, datetime
import pytz  # Add this import


# Defines a viewset for the Device model using Django REST Framework's ModelViewSet, which provides default CRUD operations.
class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all() # Specifies that all Device objects should be used as the queryset for this viewset.
    serializer_class = DeviceSerializer # Indicates that the DeviceSerializer should be used to serialize and deserialize Device objects.

class SignalViewSet(viewsets.ModelViewSet):
    queryset = Signal.objects.all()
    serializer_class = SignalSerializer

# Defines a function-based view named signals_view. Note that self should not be included for function-based views; it is only used in class-based views. This might be an error.
def signals_view(request):
    signals = Signal.objects.all() # Retrieves all Signal objects from the database.
    signals_data = json.dumps(list(signals.values('timestamp', 'value', 'signal_type', 'device__name')), cls=DjangoJSONEncoder) # Serializes the Signal objects to JSON format. 
    # The values method is used to get specific fields (timestamp, value, signal_type, and device__name) from each Signal object. 
    context = {                     # Creates a context dictionary with the serialized signals data.
            'signals': signals_data
    }
    return render(request, 'myapp/signals.html', context) # Renders the signals.html template with the context data.



def get_temperature_data(request):
    # Define Greece timezone
    greece_tz = pytz.timezone('Europe/Athens')

    # Get data from the last 10 minutes
    time_threshold = timezone.now() - datetime.timedelta(minutes=10)

    temp_sensor_1 = Signal.objects.filter(device__name="TempS_ID_1", timestamp__gte=time_threshold).order_by('timestamp')
    temp_sensor_2 = Signal.objects.filter(device__name="TempS_ID_2", timestamp__gte=time_threshold).order_by('timestamp')
    temp_sensor_3 = Signal.objects.filter(device__name="TempS_ID_3", timestamp__gte=time_threshold).order_by('timestamp')
    hum_sensor = Signal.objects.filter(device__name="HumidityS_ID_1", timestamp__gte=time_threshold).order_by('timestamp')
    
    data = {
        'labels': [signal.timestamp.astimezone(greece_tz).strftime('%H:%M:%S') for signal in temp_sensor_1],  # Convert timestamps to Greece timezone and format them
        'datasets': [
            {
                'label': 'TempS_ID_1',
                'data': [signal.value for signal in temp_sensor_1],
                'borderColor': 'black',
                'backgroundColor': 'rgba(0, 0, 0, 0.2)',
                'fill': False,
            },
            {
                'label': 'TempS_ID_2',
                'data': [signal.value for signal in temp_sensor_2],
                'borderColor': 'red',
                'backgroundColor': 'rgba(255, 0, 0, 0.2)',
                'fill': False,
            },
            {
                'label': 'TempS_ID_3',
                'data': [signal.value for signal in temp_sensor_3],
                'borderColor': 'green',
                'backgroundColor': 'rgba(0, 255, 0, 0.2)',
                'fill': False,
            },
            {
                'label': 'HumidityS_ID_1',
                'data': [signal.value for signal in hum_sensor],
                'borderColor': 'purple',
                'backgroundColor': 'rgba(128, 0, 128, 0.2)',
                'fill': False,
            },
        ]
    }
    
    return JsonResponse(data)



def temperature_chart(request):
    return render(request, 'myapp/temperature_chart.html')
