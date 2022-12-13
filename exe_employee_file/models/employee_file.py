# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EmployeeFile(models.Model):
    _inherit = ('hr.employee')

    employee_file = fields.Char('Legajo')