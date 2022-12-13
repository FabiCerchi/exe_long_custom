# -*- coding: utf-8 -*-
# from odoo import http


# class ExeLibroSueldos(http.Controller):
#     @http.route('/exe_libro_sueldos/exe_libro_sueldos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/exe_libro_sueldos/exe_libro_sueldos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('exe_libro_sueldos.listing', {
#             'root': '/exe_libro_sueldos/exe_libro_sueldos',
#             'objects': http.request.env['exe_libro_sueldos.exe_libro_sueldos'].search([]),
#         })

#     @http.route('/exe_libro_sueldos/exe_libro_sueldos/objects/<model("exe_libro_sueldos.exe_libro_sueldos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('exe_libro_sueldos.object', {
#             'object': obj
#         })
