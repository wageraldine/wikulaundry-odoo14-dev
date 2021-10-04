# -*- coding: utf-8 -*-
# from odoo import http


# class Wikulaundry(http.Controller):
#     @http.route('/wikulaundry/wikulaundry/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wikulaundry/wikulaundry/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wikulaundry.listing', {
#             'root': '/wikulaundry/wikulaundry',
#             'objects': http.request.env['wikulaundry.wikulaundry'].search([]),
#         })

#     @http.route('/wikulaundry/wikulaundry/objects/<model("wikulaundry.wikulaundry"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wikulaundry.object', {
#             'object': obj
#         })
