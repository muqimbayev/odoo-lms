from odoo import fields, models, api

class Equipment(models.Model):
    _name = "inventory.equipment"
    _description = "Educational Equipment"

    name = fields.Char(required=True)
    equipment_type = fields.Selection([
        ('computer', "Computer"),
        ('projector', "Projector"),
        ('printer', "Printer"),
        ('whiteboard', "Whiteboard"),
        ('other', "Other"),
    ], default="other")
    building_id = fields.Many2one("building.building", string="Building")
    purchase_date = fields.Date(string="Purchase Date")
    condition = fields.Selection([
        ('new', "New"),
        ('good', "Good"),
        ('maintenance', "Needs Maintenance"),
        ('broken', "Broken")
    ], default="good")
    responsible_id = fields.Many2one("res.users", string="Responsible Person")
