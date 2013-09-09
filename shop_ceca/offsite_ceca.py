#-*- coding: utf-8 -*-
from decimal import Decimal


from django.conf import settings
from django.conf.urls.defaults import patterns, url
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect

from .forms import CecaPaymentForm
from .models import CecaResponse

URL_LIVE = "https://pgw.ceca.es/cgi-bin/tpv"
URL_TEST = "http://tpv.ceca.es:8000/cgi-bin/tpv"


class OffsiteCecaBackend(object):
    backend_name = "TPV"
    url_namespace = "ceca"

    #===========================================================================
    # Defined by the backends API
    #===========================================================================

    def __init__(self, shop):
        self.shop = shop
        assert settings.SHOP_CECA, "You need to define SHOP_CECA"

    def get_urls(self):
        urlpatterns = patterns('',
            url(r'^$', self.ceca_payment_view, name='ceca' ),
            url(r'^success$', self.ceca_successful_return_view, name='ceca_success' ),
            url(r'^ipn/$', self.payment_ipn, name='ceca_ipn' ),
        )
        return urlpatterns

    #===========================================================================
    # Views
    #===========================================================================

    def _get_service_url(self):
        if 'TEST' in settings.SHOP_CECA and settings.SHOP_CECA['TEST']:
            return URL_TEST
        return URL_LIVE

    def ceca_payment_view(self, request):
        order = self.shop.get_order(request)
        order_id = self.shop.get_order_unique_id(order)
        amount = self.shop.get_order_total(order)
        description = "Order %s" % order_id

        form = CecaPaymentForm(initial={
            'Num_operacion': order_id,
            'Importe': amount,
            'Descripcion': description,
            'request': request,
            'URL_OK': request.build_absolute_uri(reverse("ceca_success")),
            'URL_NOK': request.build_absolute_uri(reverse("checkout_selection")),
        })


        # Create the instance.
        context = {
            "form": form,
            'service_url': self._get_service_url()
        }
        rc = RequestContext(request, context)
        return render_to_response("shop_ceca/payment.html", rc)


    @csrf_exempt
    def ceca_successful_return_view(self, request):
        return HttpResponseRedirect(self.shop.get_finished_url())


    #===========================================================================
    # Signal listeners
    #===========================================================================

    @csrf_exempt
    def payment_ipn(self, request):
        post_data = request.POST.copy()
        data = {}

        resp_fields = {
            'MerchantID': 'merchant_id',
            'AcquirerBIN': 'acquirer_bin',
            'TerminalID': 'terminal_id',
            'Num_operacion': 'num_operacion',
            'Importe': 'importe',
            'TipoMoneda': 'tipo_moneda',
            'Referencia': 'referencia',
            'Firma': 'firma',
            'Num_aut': 'numero_autorizacion',
            'Idioma': 'idioma',
            'Pais': 'pais',
            'Descripcion': 'descripcion',
        }

        for (key, val) in resp_fields.iteritems():
            data[val] = post_data.get(key, '')

        order = self.shop.get_order_for_id(data['num_operacion'])
        transaction_id = data['referencia']
        amount = Decimal(data['importe']) / 100
        try:
            CecaResponse.objects.create(**data)
            self.shop.confirm_payment(order, amount,
                                      transaction_id=transaction_id,
                                      payment_method=self.backend_name)

            status = "$*$OKY$*$"
        except:
            status = "FAILURE"

        return HttpResponse(status)
