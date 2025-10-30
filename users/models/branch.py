from odoo import fields, models

class Branch(models.Model):
    _inherit = "res.company"

    manager_id = fields.Many2one("lms.manager", required=True, string="Manager")
    # group_ids = fields.One2many("education.groups", inverse_name="branch_id")
    count_students = fields.Integer(string="Count students", compute="_compute_count_student")
    