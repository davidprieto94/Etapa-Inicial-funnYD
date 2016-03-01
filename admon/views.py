from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.contrib.auth import login

from admon.forms import loginAdmonForm
from app.utility import get_or_none
from usuarios.models import usuariosModel


def ingresar(request):
	return render(request, "ingresar.html")


class loginAdmonView(FormView):
	form_class = loginAdmonForm
	template_name = 'ingresar.html'
	success_url = '/admon/'

	def form_valid(self, form):
		usuario = get_or_none(usuariosModel, user=form.user_cache)
		if usuario is None:
			form.add_error(None, 'Este usuario no existe')
			return self.form_invalid(form)
		elif not usuario.user.is_active:
			form.add_error(None, 'Esta usuario no esta activo')
			return self.form_invalid(form)
		elif not usuario.user.is_staff:
			form.add_error(None, 'Este usuario no es administrador')
			return self.form_invalid(form)
		else:
			login(self.request, form.user_cache)

		return super(loginAdmonView, self).form_valid(form)

class dashBoardView(TemplateView):
	template_name = "dash_board.html"