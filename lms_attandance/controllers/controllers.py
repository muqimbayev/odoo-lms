# -*- coding: utf-8 -*-
# from odoo import http


# class LmsAttandance(http.Controller):
#     @http.route('/lms_attandance/lms_attandance', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lms_attandance/lms_attandance/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lms_attandance.listing', {
#             'root': '/lms_attandance/lms_attandance',
#             'objects': http.request.env['lms_attandance.lms_attandance'].search([]),
#         })

#     @http.route('/lms_attandance/lms_attandance/objects/<model("lms_attandance.lms_attandance"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lms_attandance.object', {
#             'object': obj
#         })

