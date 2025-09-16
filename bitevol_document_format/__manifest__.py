# __manifest__.py
{
    "name": "Bitevol Document Format",
    "version": "18.0.1.0.0",
    "summary": "Personaliza el impreso de facturas ocultando el código interno",
    "author": "Xtendoo, Dani Domínguez",
    "website": "https://www.xtendoo.es",
    "category": "Accounting",
    "license": "LGPL-3",
    "depends": ["account"],
    "data": [
        "views/report_invoice_inherit.xml",
    ],
    "installable": True,
    "application": False,
}
