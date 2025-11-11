from odoo import fields, models

class Branch(models.Model):
    _inherit = "res.company"

    group_ids = fields.One2many("education.groups", inverse_name="branch_id")
    count_students = fields.Integer(string="Count students", compute="_compute_count_student")
    count_groups = fields.Integer("Branch groups", compute="_compute_branch_groups")
    