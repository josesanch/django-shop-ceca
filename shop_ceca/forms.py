from django import forms
from django.conf import settings


import hashlib

class CecaPaymentForm(forms.Form):
    # Campos del formulario
    MerchantID = forms.CharField(widget=forms.HiddenInput(), required=False)
    AcquirerBIN = forms.CharField(widget=forms.HiddenInput(), required=False)
    TerminalID = forms.CharField(widget=forms.HiddenInput(), required=False)
    Num_operacion = forms.CharField(widget=forms.HiddenInput(), required=False)
    Importe = forms.CharField(widget=forms.HiddenInput(), required=False)
    TipoMoneda = forms.CharField(widget=forms.HiddenInput(), required=False)
    Exponente  = forms.CharField(widget=forms.HiddenInput(), required=False)
    URL_OK  = forms.CharField(widget=forms.HiddenInput(), required=False)
    URL_NOK  = forms.CharField(widget=forms.HiddenInput(), required=False)
    Firma = forms.CharField(widget=forms.HiddenInput(), required=False)
    Cifrado = forms.CharField(widget=forms.HiddenInput(), required=False)
    Idioma = forms.CharField(widget=forms.HiddenInput(), required=False)
    Pago_soportado = forms.CharField(widget=forms.HiddenInput(), required=False)
    Descripcion = forms.CharField(widget=forms.HiddenInput(), required=False)

    def __init__(self, *args, **kwargs):
        super(CecaPaymentForm, self).__init__(*args, **kwargs)

        if self.initial:
            self.settings = settings.SHOP_CECA
            self.valores_por_defecto()
            self.generar_firma()


    def valores_por_defecto(self):
        self.initial['MerchantID'] = self.settings['merchant_id']
        self.initial['AcquirerBIN'] = self.settings['acquirer_bin']
        self.initial['TerminalID'] = self.settings['terminal_id']
        self.initial['Exponente'] = 2

        if not hasattr(self.initial, 'TipoMoneda'):
            self.initial['TipoMoneda'] = 978


        if not hasattr(self.initial, 'Idioma'):
            self.initial['Idioma'] = 1

        self.initial['Importe'] = int(self.initial['Importe'] * 100)
        self.initial['Cifrado'] = "SHA1"
        self.initial['Pago_soportado'] = "SSL"



    def generar_firma(self):
        string = "%s%s%s%s%s%s%s%s%s%s%s" % (
            self.settings['clave_encriptacion'],
            self.initial['MerchantID'],
            self.initial['AcquirerBIN'],
            self.initial['TerminalID'],
            self.initial['Num_operacion'],
            self.initial['Importe'],
            self.initial['TipoMoneda'],
            self.initial['Exponente'],
            self.initial['Cifrado'],
            self.initial['URL_OK'],
            self.initial['URL_NOK'],
        )

        self.initial['Firma'] = hashlib.sha1(string).hexdigest()
