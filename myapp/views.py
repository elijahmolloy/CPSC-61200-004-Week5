from django.http import HttpResponse
from django.shortcuts import render

TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates")'
)

# Create your views here.
def index(request):
    return render(request, "index.html")