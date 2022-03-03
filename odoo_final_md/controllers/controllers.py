# -*- coding: utf-8 -*-
# from odoo import http


# class OdooFinalMd(http.Controller):
#     @http.route('/odoo_final_md/odoo_final_md/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_final_md/odoo_final_md/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_final_md.listing', {
#             'root': '/odoo_final_md/odoo_final_md',
#             'objects': http.request.env['odoo_final_md.odoo_final_md'].search([]),
#         })

#     @http.route('/odoo_final_md/odoo_final_md/objects/<model("odoo_final_md.odoo_final_md"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_final_md.object', {
#             'object': obj
#         })
