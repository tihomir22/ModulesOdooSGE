# -*- coding: utf-8 -*-
from odoo import http

# class Papito(http.Controller):
#     @http.route('/papito/papito/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/papito/papito/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('papito.listing', {
#             'root': '/papito/papito',
#             'objects': http.request.env['papito.papito'].search([]),
#         })

#     @http.route('/papito/papito/objects/<model("papito.papito"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('papito.object', {
#             'object': obj
#         })