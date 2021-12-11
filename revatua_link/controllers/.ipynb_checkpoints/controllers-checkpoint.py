# -*- coding: utf-8 -*-
# from odoo import http


# class RevatuaLink(http.Controller):
#     @http.route('/revatua_link/revatua_link', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/revatua_link/revatua_link/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('revatua_link.listing', {
#             'root': '/revatua_link/revatua_link',
#             'objects': http.request.env['revatua_link.revatua_link'].search([]),
#         })

#     @http.route('/revatua_link/revatua_link/objects/<model("revatua_link.revatua_link"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('revatua_link.object', {
#             'object': obj
#         })
