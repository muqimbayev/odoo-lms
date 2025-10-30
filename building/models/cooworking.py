from odoo import fields, models


class Coworking(models.Model):
    _name = "building.coworking"
    _description = "Coworing"

    name = fields.Char(required=True)
    is_available = fields.Boolean(default=True, compute="_compute_is_available")
    current_user_id = fields.Many2one("res.partner", string="Current User")
    max_capacity = fields.Integer(string="Capacity")