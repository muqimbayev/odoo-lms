from odoo import fields, models

class GroupRoom(models.Model):
    _inherit = "education.groups"

    classroom_id = fields.Many2one("building.room", string="Classroom")
