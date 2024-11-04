
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin,\
     PermissionRequiredMixin
from django.views import generic

#from .models import Idioma,Frase

class MixinFormInvalid:
    def form_invalid(self,form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            # Manejo específico para solicitudes AJAX/en versiones posteriores de  Django al del curso cambia esto
            return JsonResponse({'error': 'Error al procesar el formulario'}, status=400)
        else:
            return super().form_invalid(form)

class SinPrivilegios(LoginRequiredMixin, PermissionRequiredMixin, MixinFormInvalid):
    login_url = 'bases:login'
    raise_exception=False
    redirect_field_name="redirecto_to"

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user==AnonymousUser():
            self.login_url='bases:sin_privilegios'
        return HttpResponseRedirect(reverse_lazy(self.login_url))


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'bases/home.html'
    login_url='bases:login'


class HomeSinPrivilegios(LoginRequiredMixin, generic.TemplateView):
    login_url = "bases:login"
    template_name="bases/sin_privilegios.html"

"""
class IdiomaList(generic.ListView):
    template_name = "bases/idiomas.html"
    model = Idioma
    context_object_name="obj"



class FraseList(generic.ListView):
    template_name = "bases/frases.html"
    model = Frase
    context_object_name="obj"

    def get_queryset(self):
        qs = Frase.objects.all()
        idioma_id = self.request.GET.get("lang")
        if idioma_id:
            qs = qs.filter(idioma__id=idioma_id)
        return qs
"""