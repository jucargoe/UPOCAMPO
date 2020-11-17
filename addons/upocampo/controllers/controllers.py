# -*- coding: utf-8 -*-
# from odoo import http


# class Upocampo(http.Controller):
#     @http.route('/upocampo/upocampo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/upocampo/upocampo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('upocampo.listing', {
#             'root': '/upocampo/upocampo',
#             'objects': http.request.env['upocampo.upocampo'].search([]),
#         })

#     @http.route('/upocampo/upocampo/objects/<model("upocampo.upocampo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('upocampo.object', {
#             'object': obj
#         })
