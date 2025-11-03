from odoo import fields, models

class TeacherAddCustom(models.Model):
    _inherit = "users.teacher"
       
    subject_ids = fields.Many2many(comodel_name="education.subjects", required=True)
    group_ids = fields.Many2many(comodel_name="education.groups")




