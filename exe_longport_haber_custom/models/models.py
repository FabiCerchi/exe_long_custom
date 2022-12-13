# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class exe_longport_haber_custom(models.Model):
#     _name = 'exe_longport_haber_custom.exe_longport_haber_custom'
#     _description = 'exe_longport_haber_custom.exe_longport_haber_custom'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
