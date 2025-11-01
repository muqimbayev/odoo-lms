from odoo import fields, models


class MaterialPayment(models.Model):
    _name = "payment.material.payment"
    _description = "Material Payment"

    requirement_id = fields.Many2one("inventory.requirement")
    price = fields.Float(string="Price")
    payment_date = fields.Date(default=fields.Date.today)
    payment_state = fields.Selection([
        ('unpaid', "Unpaid"),
        ('paid', "Paid")
    ], default='unpaid')
