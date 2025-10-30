# -*- coding: utf-8 -*-
# from odoo import http


# class LearningManagmentSystem(http.Controller):
#     @http.route('/learning_managment_system/learning_managment_system', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/learning_managment_system/learning_managment_system/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('learning_managment_system.listing', {
#             'root': '/learning_managment_system/learning_managment_system',
#             'objects': http.request.env['learning_managment_system.learning_managment_system'].search([]),
#         })

#     @http.route('/learning_managment_system/learning_managment_system/objects/<model("learning_managment_system.learning_managment_system"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('learning_managment_system.object', {
#             'object': obj
#         })

