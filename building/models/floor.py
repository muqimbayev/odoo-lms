from odoo import fields, models


class Floor(models.Model):
    _name = "building.floor"
    _description = "Floor"

    name = fields.Char(required=True)
    number = fields.Integer(string="Floor Number", required=True)
    building_id = fields.Many2one("building.building", required=True, string="Building")
    room_ids = fields.One2many("building.room", "floor_id", string="Rooms")
