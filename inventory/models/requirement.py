from odoo import fields, models, api

class Requirement(models.Model):
    _name = "inventory.requirement"
    _description = "Educational Requirements"

    name = fields.Char(required=True)
    category = fields.Selection([
        ('material', "Material"),
        ('equipment', "Equipment"),
        ('service', "Service"),
        ('other', "Other")
    ], default="material")
    quantity = fields.Integer(default=1)
    request_date = fields.Date(default=fields.Date.today)
    requested_by = fields.Many2one("res.users", string="Requested By")
    branch_id = fields.Many2one("res.company", string="Branch")
    status = fields.Selection([
        ('draft', "Draft"),
        ('approved', "Approved"),
        ('purchased', "Purchased"),
        ('rejected', "Rejected")
    ], default="draft")
    description = fields.Text()
