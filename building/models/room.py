from odoo import fields, models


class Room(models.Model):
    _name = "building.room"
    _description = "Room"

    name = fields.Char(required=True)
    building_id = fields.Many2one("building.building", string="Building", required=True)
    floor_id = fields.Many2one("building.floor", string="Floor")
    capacity = fields.Integer(string="Capacity")
    type = fields.Selection([
        ('classroom', "Classroom"),
        ('office', "Office"),
        ('coworking', "Coworking Space"),
    ], default='classroom')
    active = fields.Boolean(default=True)
