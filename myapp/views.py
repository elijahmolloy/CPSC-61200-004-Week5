from django.http import HttpResponse
from django.shortcuts import render
import datetime

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)

# Create your views here.
def index(request):
    variables = {
        "current_date": datetime.datetime.now().date()
    }
    
    return render(request, "index.html", variables)