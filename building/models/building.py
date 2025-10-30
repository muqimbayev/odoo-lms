from odoo import fields, models


class Building(models.Model):
    _name = "building.building"
    _description = "Building"

    name = fields.Char(required=True)
    address = fields.Char()
    branch_id = fields.Many2one("res.company", string="Branch")
    floor_count = fields.Integer(string="Floors")
    room_ids = fields.One2many("building.room", "building_id", string="Rooms")
