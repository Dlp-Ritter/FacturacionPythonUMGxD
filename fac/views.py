from django.shortcuts import render#,redirect

from django.views import generic

#from django.contrib.messages.views import SuccessMessageMixin
#from django.urls import reverse_lazy
#from django.contrib.auth.decorators import login_required, permission_required
#from django.http import HttpResponse
#from datetime import datetime
#from django.contrib import messages

from django.contrib.auth import authenticate

from bases.views import SinPrivilegios

from .models import Cliente#, FacturaEnc, FacturaDet
#from .forms import ClienteForm
#import inv.views as inv
#from inv.models import Producto

class ClienteView(SinPrivilegios, generic.ListView):
    model = Cliente
    template_name = "fac/cliente_list.html"
    context_object_name = "obj"
    permission_required="cmp.view_cliente"
