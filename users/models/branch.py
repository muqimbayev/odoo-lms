from odoo import fields, models

class Branch(models.Model):
    _inherit = "res.company"

    manager_id = fields.Many2one("lms.manager", required=True, string="Manager")
