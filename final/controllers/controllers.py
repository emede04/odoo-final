# -*- coding: utf-8 -*-
# from odoo import http


# class Final(http.Controller):
#     @http.route('/final/final/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/final/final/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('final.listing', {
#             'root': '/final/final',
#             'objects': http.request.env['final.final'].search([]),
#         })

#     @http.route('/final/final/objects/<model("final.final"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('final.object', {
#             'object': obj
#         })
