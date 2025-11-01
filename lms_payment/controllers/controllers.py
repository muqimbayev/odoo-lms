# -*- coding: utf-8 -*-
# from odoo import http


# class LmsPayment(http.Controller):
#     @http.route('/lms_payment/lms_payment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lms_payment/lms_payment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lms_payment.listing', {
#             'root': '/lms_payment/lms_payment',
#             'objects': http.request.env['lms_payment.lms_payment'].search([]),
#         })

#     @http.route('/lms_payment/lms_payment/objects/<model("lms_payment.lms_payment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lms_payment.object', {
#             'object': obj
#         })

