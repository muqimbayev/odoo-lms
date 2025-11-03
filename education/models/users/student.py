from odoo import fields, models, api


class StudentAddCustom(models.Model):
    _inherit = "users.students"

    group_ids = fields.Many2many(comodel_name="education.groups", string="group")
    certification_ids = fields.One2many(comodel_name="education.certification")





