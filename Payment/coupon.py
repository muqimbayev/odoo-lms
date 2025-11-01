from odoo import fields, models


class Coupon(models.Model):
    _name = "payment.coupon"
    _description = "Discount Coupon"

    code = fields.Char(required=True)
    discount_percent = fields.Float(default=0)
    valid_from = fields.Date(default=fields.Date.today)
    valid_to = fields.Date()
    usage_limit = fields.Integer(default=1)
    used_count = fields.Integer(default=0)
    active = fields.Boolean(default=True)
