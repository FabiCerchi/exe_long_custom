# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrEmployeeRelativeCustom(models.Model):
    _inherit = 'hr.employee.relative'
    
    identification_id = fields.Char(string = 'CUIL')