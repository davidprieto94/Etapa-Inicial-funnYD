from django.shortcuts import render

def listActividades(request):	
	return render(request, "list_actividades.html")

def descripcionRD(request):	
	return render(request, "descr_rutinadiaria.html")