from django.shortcuts import render

def listActividades(request):	
	return render(request, "list_actividades.html")