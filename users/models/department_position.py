from odoo import fields, models


class Department(models.Model):
    _name = "users.department"
    _description = "Department"

    name = fields.Char(string="Name", required=True)
    chief_id = fields.Many2one(comodel_name="res.users", string="Chief")


class Positions(models.Model):
    _name = "users.positions"
    _description = "Positions"

    name = fields.Char(string="Position", required=True)
    hiring_date = fields.Date(string="Hiring date", required=True)
    released_date = fields.Date(string="released")
    is_active = fields.Boolean(string="Active", default=True)
    
    



    