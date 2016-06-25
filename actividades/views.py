from django.shortcuts import render
from actividades.models import actividadesModel



def listActividades(request):	
	
	actividades = actividadesModel.objects.all()
	context = {
		'actividades' : actividades,
	}

	return render(request, "list_actividades.html", context)

def descripcionRD(request):	
	return render(request, "descr_rutinadiaria.html")