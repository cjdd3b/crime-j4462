from data.models import Crime
from django.shortcuts import render_to_response


# Remember: Django views are simply functions that accept a HTTP request as an argument
def index(request):
    # First we're going to get a list of all the crimes in our dataset
    all_crimes = Crime.objects.all()

    # If we wanted to get crimes of a certain type, we could employ Django's filtering functionality.
    # Say we wanted all the crimes of type 'TRAFFIC'. That might look like this:
    # traffic_crimes = Crime.objects.filter(type='TRAFFIC')

    # Either way, now we're going to send them to a template using Django's render_to_response shortcut
    return render_to_response('index.html', {'crimes': all_crimes})


def detail(request, crime_id):
    # In this example, we're going to get a single crime from the database
    crime = Crime.objects.get(incident_num=crime_id)

    # ... and we'll send it to a different template in exactly the same way as above
    return render_to_response('crime_detail.html', {'crime': crime})