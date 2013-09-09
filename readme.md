====================
django-shop-ceca
====================

This module is a payment backend module for django-SHOP, for the CECA Tpv

Installation
============
Using pip::

    pip install django-shop-ceca

TPV Configuration in django shop
====================

In order to shop ceca to work, you will need to include 'shop_ceca' in your INSTALLED_APP

INSTALLED_APP = (
  ...
  'shop_ceca'
)

After that, you will need to especify the tpv configuration in settings

SHOP_CECA = {
    "merchant_id": "...",
    "acquirer_bin": "...",
    "clave_encriptacion": "....",
    "terminal_id": "....",
    'TEST': True  # Set to true if you want the test eviroment.
}


* Shop configuration
Add 'shop_ceca.offsite_ceca.OffsiteCecaBackend' to SHOP_PAYMENT_BACKENDS

SHOP_PAYMENT_BACKENDS = (
  'shop_ceca.offsite_ceca.OffsiteCecaBackend',
)


Changes
====================
0.1.0: First release to the public.
