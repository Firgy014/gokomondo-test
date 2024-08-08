# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderCustom(http.Controller):
#     @http.route('/sale_order_custom/sale_order_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_custom/sale_order_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_custom.listing', {
#             'root': '/sale_order_custom/sale_order_custom',
#             'objects': http.request.env['sale_order_custom.sale_order_custom'].search([]),
#         })

#     @http.route('/sale_order_custom/sale_order_custom/objects/<model("sale_order_custom.sale_order_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_custom.object', {
#             'object': obj
#         })
