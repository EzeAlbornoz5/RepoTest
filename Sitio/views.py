from django.shortcuts import render, redirect

from Sitio.models import Noticia
from datetime import datetime
from Sitio.forms import LoginForm, NoticiaForm

# Create your views here.

def inicio(request):
	nueva = Noticia()
	nueva.titulo = 'Entro alguien!'
	nueva.texto = 'Acaba de entrar alguien al sitio...'
	nueva.fecha = datetime.now()
	nueva.save()

	noticias = Noticia.objects.all()[:3]

	return render(request, 'inicio.html', {'lista_noticias': noticias})

def LoginFake(request):
	if request.method == 'POST':
		login_form = LoginForm(request.POST)

		if login_form.is_valid():
			return redirect('/inicio/')
	else:
		login_form = LoginForm()

	return render(request, 'login_fake.html', {'form': login_form})


def CrearNoticia(request):
	if request.method == 'POST':
		noticia_form = NoticiaForm(request.POST)

		if noticia_form.is_valid():
			noticia = noticia_form.save(commit=False)
			noticia.fecha = datetime.now()
			noticia.save()

			return redirect('/inicio/')
	else:
		noticia_form = NoticiaForm()

	return render(request, 'crear_noticia.html', {'form': noticia_form})

