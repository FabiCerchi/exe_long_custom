# -*- coding: utf-8 -*-
# from odoo import http


# class ExeLongportHaberCustom(http.Controller):
#     @http.route('/exe_longport_haber_custom/exe_longport_haber_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/exe_longport_haber_custom/exe_longport_haber_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('exe_longport_haber_custom.listing', {
#             'root': '/exe_longport_haber_custom/exe_longport_haber_custom',
#             'objects': http.request.env['exe_longport_haber_custom.exe_longport_haber_custom'].search([]),
#         })

#     @http.route('/exe_longport_haber_custom/exe_longport_haber_custom/objects/<model("exe_longport_haber_custom.exe_longport_haber_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('exe_longport_haber_custom.object', {
#             'object': obj
#         })
