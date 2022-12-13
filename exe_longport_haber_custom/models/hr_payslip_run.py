# -*- coding: utf-8 -*-

from odoo import models, fields, api

PAGO_ART12 = [
    ('transfer', 'Interbanking'),
    ('cash', 'Efectivo'),
]

class HrPayslipRunCustom(models.Model):
    _inherit = 'hr.payslip.run'
        
    despositado_art12 = fields.Selection(PAGO_ART12,default=PAGO_ART12[0][0],required=True,string="Depositado en")
    fecha_pago_art12 = fields.Date(required=True,string='Fecha')
    periodo_pago_art12 = fields.Date(required=True,string="Periodo")