from django.db import models


class CecaResponse(models.Model):
    # merchant details
    merchant_id = models.CharField(max_length=25)
    acquirer_bin = models.CharField(max_length=25, blank=True, null=True)
    terminal_id = models.CharField(max_length=25, blank=True, null=True)

    # purchase details
    num_operacion = models.CharField(max_length=50, blank=True, null=True)
    importe  = models.CharField(max_length=50, blank=True, null=True)
    tipo_moneda   = models.CharField(max_length=50, blank=True, null=True)
    referencia  = models.CharField(max_length=50, blank=True, null=True)
    firma  = models.CharField(max_length=50, blank=True, null=True)
    numero_autorizacion  = models.CharField(max_length=50, blank=True, null=True)
    idioma  = models.CharField(max_length=50, blank=True, null=True)
    pais  = models.CharField(max_length=50, blank=True, null=True)
    descripcion  = models.CharField(max_length=50, blank=True, null=True)

    def __unicode__(self):
        return self.descripcion
