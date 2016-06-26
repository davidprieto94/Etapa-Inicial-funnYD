from django.shortcuts import render

def inicio(request):
	return render(request,'inicio.html')

def registro(request):	
	return render(request, "registro.html")







def cambiocontraseña(request):	
	return render(request, "cambiocontraseña.html")