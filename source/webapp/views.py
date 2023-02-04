from django.shortcuts import render
from webapp.get_map import get_coordinates
from django.template.exceptions import TemplateDoesNotExist


def get_number(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        context = {
            "number": request.POST.get('number')
        }
        try:
            get_coordinates(context['number'])
            return render(request, "our_map.html", context)
        except (FileNotFoundError, NameError, TemplateDoesNotExist):
            return render(request, "server_error.html", context)
