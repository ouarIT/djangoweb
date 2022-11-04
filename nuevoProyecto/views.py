from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader


def home_page(request):
    doc_externo = loader.get_template("index.html")

    # creamos el documento
    documento = doc_externo.render()
    return HttpResponse(documento)
